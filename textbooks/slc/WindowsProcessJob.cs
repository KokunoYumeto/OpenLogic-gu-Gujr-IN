using System;
using System.Runtime.InteropServices;
using System.Diagnostics;
using System.ComponentModel;
public static class SlcProcessJob {
 [DllImport("kernel32.dll",CharSet=CharSet.Unicode)] public static extern IntPtr CreateJobObject(IntPtr attrs,string name);
 [DllImport("kernel32.dll",SetLastError=true)] public static extern bool AssignProcessToJobObject(IntPtr job,IntPtr process);
 [DllImport("kernel32.dll")] public static extern bool TerminateJobObject(IntPtr job,uint code);
 [DllImport("kernel32.dll")] public static extern bool CloseHandle(IntPtr h);
 [StructLayout(LayoutKind.Sequential)] public struct Accounting {
 public long a,b,c,d; public uint faults,total,active,terminated;
 }
 [DllImport("kernel32.dll",SetLastError=true)] public static extern bool QueryInformationJobObject(IntPtr job,int info,out Accounting data,uint size,IntPtr ret);
 public static uint Active(IntPtr job) {
 Accounting a;
 if(!QueryInformationJobObject(job,1,out a,(uint)Marshal.SizeOf(typeof(Accounting)),IntPtr.Zero)) throw new Exception("Job accounting unavailable");
 return a.active;
 }
 [StructLayout(LayoutKind.Sequential)] public struct Security { public int length; public IntPtr descriptor; public int inherit; }
 [StructLayout(LayoutKind.Sequential,CharSet=CharSet.Unicode)] public struct Startup {
 public int cb; public string reserved,desktop,title; public uint x,y,xSize,ySize,xChars,yChars,fill,flags;
 public ushort show,reserved2; public IntPtr reservedPtr,input,output,error;
 }
 [StructLayout(LayoutKind.Sequential)] public struct ProcessInfo { public IntPtr process,thread; public uint pid,tid; }
 [DllImport("kernel32.dll",CharSet=CharSet.Unicode,SetLastError=true)] static extern IntPtr CreateFile(string name,uint access,uint share,ref Security security,uint disposition,uint attributes,IntPtr template);
 [DllImport("kernel32.dll",CharSet=CharSet.Unicode,SetLastError=true)] static extern bool CreateProcess(string application,System.Text.StringBuilder command,IntPtr pa,IntPtr ta,bool inherit,uint flags,IntPtr environment,string directory,ref Startup startup,out ProcessInfo info);
 [DllImport("kernel32.dll",SetLastError=true)] static extern uint ResumeThread(IntPtr thread);
 [DllImport("kernel32.dll")] static extern bool TerminateProcess(IntPtr process,uint code);
 [DllImport("kernel32.dll")] static extern uint WaitForSingleObject(IntPtr handle,uint milliseconds);
 public static Process Launch(string exe,string args,string cwd,IntPtr job,string outputFile) {
 Security sa=new Security{length=Marshal.SizeOf(typeof(Security)),inherit=1};
 IntPtr output=CreateFile(outputFile,0x40000000,1,ref sa,2,0,IntPtr.Zero);
 if(output==new IntPtr(-1)) throw new Win32Exception(Marshal.GetLastWin32Error());
 ProcessInfo pi=new ProcessInfo();
 try {
 Startup si=new Startup{cb=Marshal.SizeOf(typeof(Startup)),flags=0x100,output=output,error=output,input=IntPtr.Zero};
 var command=new System.Text.StringBuilder("\""+exe+"\" "+args);
 if(!CreateProcess(exe,command,IntPtr.Zero,IntPtr.Zero,true,0x08000004,IntPtr.Zero,cwd,ref si,out pi)) throw new Win32Exception(Marshal.GetLastWin32Error());
 if(!AssignProcessToJobObject(job,pi.process)) {
 int err=Marshal.GetLastWin32Error();TerminateProcess(pi.process,125);WaitForSingleObject(pi.process,10000);
 throw new Win32Exception(err,"Suspended TeX process was not captured; it never ran.");
 }
 var process=Process.GetProcessById((int)pi.pid);
 var retainedHandle=process.Handle;
 if(ResumeThread(pi.thread)==0xffffffff) {
 TerminateJobObject(job,125);WaitForSingleObject(pi.process,10000);process.Dispose();
 throw new Win32Exception(Marshal.GetLastWin32Error(),"Could not resume captured TeX process");
 }
 return process;
 } finally {
 CloseHandle(output);
 if(pi.thread!=IntPtr.Zero) CloseHandle(pi.thread);
 if(pi.process!=IntPtr.Zero) CloseHandle(pi.process);
 }
 }
}
