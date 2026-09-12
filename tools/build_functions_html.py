"""Build the cumulative Gujarati HTML readers and their QA receipts."""
from pathlib import Path
import re,json,subprocess,html,hashlib,sys
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1];B=R/'build';O=R/'reader'
edition=sys.argv[1] if len(sys.argv)>1 else 'functions'
assert edition in {'functions','size','arithmetization','infinite','propositional','proof-systems','sequent-calculus','natural-deduction','tableaux','axiomatic-deduction','completeness','first-order-introduction','first-order-syntax'}
coverage={'functions':23,'size':37,'arithmetization':45,'infinite':51,'propositional':59,'proof-systems':65,'sequent-calculus':80,'natural-deduction':94,'tableaux':108,'axiomatic-deduction':122,'completeness':134,'first-order-introduction':145,'first-order-syntax':155}[edition]
coverage_gu={'functions':'૨૩','size':'૩૭','arithmetization':'૪૫','infinite':'૫૧','propositional':'૫૯','proof-systems':'૬૫','sequent-calculus':'૮૦','natural-deduction':'૯૪','tableaux':'૧૦૮','axiomatic-deduction':'૧૨૨','completeness':'૧૩૪','first-order-introduction':'૧૪૫','first-order-syntax':'૧૫૫'}[edition]
title={
    'functions':'ગણો, સંબંધો અને વિધેયો — ઓપન લોજિક ગુજરાતી',
    'size':'ગણો, સંબંધો, વિધેયો અને ગણોનું કદ — ઓપન લોજિક ગુજરાતી',
    'arithmetization':'ગણો, સંબંધો, વિધેયો, ગણોનું કદ અને અંકગણિતીકરણ — ઓપન લોજિક ગુજરાતી',
    'infinite':'ગણો, સંબંધો, વિધેયો, ગણોનું કદ, અંકગણિતીકરણ અને અનંત ગણો — ઓપન લોજિક ગુજરાતી',
    'propositional':'ગણો અને વિધાનાત્મક તર્કશાસ્ત્ર — ઓપન લોજિક ગુજરાતી',
    'proof-systems':'ગણો, વિધાનાત્મક તર્કશાસ્ત્ર અને નિષ્પત્તિ તંત્રો — ઓપન લોજિક ગુજરાતી',
    'sequent-calculus':'સિક્વન્ટ કલન સહિત ઓપન લોજિક ગુજરાતી',
    'natural-deduction':'સ્વાભાવિક નિગમન સહિત ઓપન લોજિક ગુજરાતી',
    'tableaux':'ટેબ્લો સહિત ઓપન લોજિક ગુજરાતી',
    'axiomatic-deduction':'સ્વયંસિદ્ધિમૂલક નિષ્પત્તિ સહિત ઓપન લોજિક ગુજરાતી',
    'completeness':'પૂર્ણતા પ્રમેય સહિત ઓપન લોજિક ગુજરાતી',
    'first-order-introduction':'પ્રથમ-ક્રમ પરિચય સહિત ઓપન લોજિક ગુજરાતી',
    'first-order-syntax':'પ્રથમ-ક્રમ વાક્યરચના સહિત ઓપન લોજિક ગુજરાતી',
}[edition]
def arg(t,i):
    while t[i].isspace():i+=1
    assert t[i]=='{',(t[i:i+40],i)
    d=1;j=i+1
    while d:
        if t[j]=='{' and t[j-1]!='\\':d+=1
        if t[j]=='}' and t[j-1]!='\\':d-=1
        j+=1
    return t[i+1:j-1],j
def command(t,name,n,callback):
    pat=re.compile(r'\\'+name+r'(?![A-Za-z])');pos=0
    while (m:=pat.search(t,pos)):
        vals=[];j=m.end()
        for _ in range(n):v,j=arg(t,j);vals.append(v)
        repl=callback(*vals);t=t[:m.start()]+repl+t[j:];pos=m.start()+len(repl)
    return t
body=(B/f'{edition}-body.tex').read_text(encoding='utf-8')
available=set(json.loads((B/f'{edition}-available-labels.json').read_text()))
body=command(body,'oliflabeldef',3,lambda key,yes,no:yes if key in available else no)
body=command(body,'sourcecorrection',2,lambda ident,note:'\n\n'+r'\begin{quote}\textbf{સ્રોત-સુધારો '+ident+'.} '+note+r'\end{quote}'+'\n\n')
# Pandoc drops ``\string`` inside ``\texttt``.  Preserve the literal macro
# name used by the OLTAB-006/007 correction disclosures without invoking the
# argument-taking source macro.
for literal in ('sFmla','item','iftag','top'):
    body=body.replace(
        '\\texttt{\\string\\'+literal+'}',
        '\\texttt{\\textbackslash{}'+literal+'}',
    )
body=body.replace(
    r'\texttt{\string\iftag\{FOL\}}',
    r'\texttt{\textbackslash{}iftag\{FOL\}}',
)
token_words={'enumerable':'ગણનીય','nonenumerable':'અગણનીય',
             'formula':'સૂત્ર','valuation':'સત્યમૂલ્ય-નિયુક્તિ',
             'derivation':'નિષ્પત્તિ','derivability':'નિષ્પન્નક્ષમતા',
             'identity':'તાદાત્મ્ય','tableau':'ટેબ્લો','sentence':'વાક્ય',
             'main operator':'મુખ્ય કારક','subformula':'ઉપસૂત્ર','variable':'ચલ'}
def token_value(namespace,key):
    if edition in {'proof-systems','sequent-calculus','natural-deduction','tableaux','axiomatic-deduction','completeness','first-order-introduction','first-order-syntax'} and namespace=='P' and key=='derivation':return 'નિષ્પત્તિઓ'
    return token_words[key]
body=command(body,'usetoken',2,token_value)
body=command(body,'printtoken',2,token_value)
body=command(body,'article',1,lambda _value:'')
if edition in {'propositional','proof-systems','sequent-calculus','natural-deduction','tableaux','axiomatic-deduction','completeness','first-order-introduction','first-order-syntax'}:
    # Expand the two xparse-style constructs that Pandoc's LaTeX reader cannot
    # define through ordinary \newcommand declarations.  The prepared source
    # has already selected the frozen upstream default connective profile.
    body=body.replace(r'\indcase*',r'\indcasestar')
    body=command(body,'indcasestar',3,lambda formula,_complex_formula,case_text:
                 '$'+formula+'$ આણ્વિક છે: '+case_text.replace(r'\indfrmp',formula).replace(r'\indfrm',formula))
    body=command(body,'indcase',3,lambda formula,complex_formula,case_text:
                 '$'+formula+r' \ident '+complex_formula+'$: '+case_text.replace(r'\indfrmp',formula).replace(r'\indfrm',formula))
    body=body.replace(r'\pSat/',r'\pNotSat')
    body=command(body,'pNotSat',2,lambda valuation,formula:
                 r'\mathfrak{'+valuation+r'}\nvDash '+formula)
    body=command(body,'pSat',2,lambda valuation,formula:
                 r'\mathfrak{'+valuation+r'}\vDash '+formula)
proof_render_receipts=[]
if edition in {'proof-systems','sequent-calculus','natural-deduction','tableaux','axiomatic-deduction','completeness','first-order-introduction','first-order-syntax'}:
    proofs=re.findall(r'\\begin\{prooftree\}[\s\S]*?\\end\{prooftree\}',body)
    tableaux=re.findall(r'\\begin\{oltableau\}[\s\S]*?\\end\{oltableau\}',body)
    derivations=re.findall(r'\\begin\{derivation\}[\s\S]*?\\end\{derivation\}',body)
    expected_proofs={'proof-systems':2,'sequent-calculus':60,'natural-deduction':123,'tableaux':124,'axiomatic-deduction':124,'completeness':124,'first-order-introduction':124,'first-order-syntax':124}[edition]
    expected_tableaux=45 if edition in {'tableaux','axiomatic-deduction','completeness','first-order-introduction','first-order-syntax'} else 1
    expected_derivations=6 if edition in {'axiomatic-deduction','completeness','first-order-introduction','first-order-syntax'} else 1
    assert (len(proofs)==expected_proofs and len(tableaux)==expected_tableaux and len(derivations)==expected_derivations), (len(proofs), len(tableaux), len(derivations), expected_proofs, expected_tableaux, expected_derivations)
    rendered_proofs=[
        r'''\[
\begin{array}{cl}
\varphi \Sequent \varphi & \\
\hline
\varphi \land \psi \Sequent \varphi & \LeftR{\land}\\
\hline
\Sequent (\varphi \land \psi) \lif \varphi & \RightR{\lif}
\end{array}
\]''',
        r'''\[
\begin{array}{cl}
[\varphi \land \psi]^1 & \\
\hline
\varphi & \Elim{\land}\\
\hline
(\varphi \land \psi) \lif \varphi & \Intro{\lif},1
\end{array}
\]''',
    ]
    for source,rendered in zip(proofs[:2],rendered_proofs):
        body=body.replace(source,rendered,1)
        proof_render_receipts.append(dict(
            kind='prooftree',
            source_sha256=hashlib.sha256(source.encode('utf-8')).hexdigest(),
            representation='MathML inference array preserving premises, conclusions and rule labels.',
        ))
    rendered_tableau=r'''\[
\begin{array}{rcl}
1.&\sFmla{\False}{(\varphi \land \psi) \lif \varphi}&\text{ધારણા}\\
2.&\sFmla{\True}{\varphi \land \psi}&\TRule{\False}{\lif}[1]\\
3.&\sFmla{\False}{\varphi}&\TRule{\False}{\lif}[1]\\
4.&\sFmla{\True}{\varphi}&\TRule{\True}{\land}[2]\\
5.&\sFmla{\True}{\psi}&\TRule{\True}{\land}[2]\quad\times
\end{array}
\]'''
    body=body.replace(tableaux[0],rendered_tableau,1)
    proof_render_receipts.append(dict(
        kind='closed_tableau',
        source_sha256=hashlib.sha256(tableaux[0].encode('utf-8')).hexdigest(),
        representation='MathML one-branch closed tableau preserving all five signed formulas, rule references and closure mark.',
    ))
    for source in derivations:
        payload=re.search(
            r'\\begin\{derivation\}([\s\S]*?)\\end\{derivation\}',source
        )[1]
        rows=len(re.findall(r'(?m)^\s*(?:\d+\.|&)',payload))
        assert rows>0 and '&' in payload
        rendered=(r'\begin{center}\begin{tabular}{rll}' + payload
                  + r'\end{tabular}\end{center}')
        body=body.replace(source,rendered,1)
        proof_render_receipts.append(dict(
            kind='axiomatic_derivation',
            source_sha256=hashlib.sha256(source.encode('utf-8')).hexdigest(),
            table_rows=rows,
            representation='HTML table preserving line numbers, formulas, continuation rows and justifications.',
        ))
    if edition=='proof-systems':
        assert not re.search(r'\\begin\{(?:prooftree|oltableau|derivation)\}',body)

if edition in {'sequent-calculus','natural-deduction','tableaux','axiomatic-deduction','completeness','first-order-introduction','first-order-syntax'}:
    def bracket_arg(t,i):
        while i<len(t) and t[i].isspace():i+=1
        if i>=len(t) or t[i]!='[':return None,i
        d=1;j=i+1
        while d:
            assert j<len(t),(t[i:i+120],i)
            if t[j]=='[' and t[j-1]!='\\':d+=1
            elif t[j]==']' and t[j-1]!='\\':d-=1
            j+=1
        return t[i+1:j-1],j
    def expand_optional_command(t,name,callback):
        pat=re.compile(r'\\'+name+r'(?![A-Za-z])');pos=0
        while (m:=pat.search(t,pos)):
            j=m.end();slash=False
            if j<len(t) and t[j]=='/':slash=True;j+=1
            args=[]
            while True:
                value,end=bracket_arg(t,j)
                if value is None:break
                args.append(value);j=end
            repl=callback(slash,args)
            t=t[:m.start()]+repl+t[j:];pos=m.start()
        return t
    def expand_sat(t):
        pat=re.compile(r'\\Sat(?![A-Za-z])');pos=0
        while (m:=pat.search(t,pos)):
            j=m.end();neg=False
            if j<len(t) and t[j]=='/':neg=True;j+=1
            structure,j=arg(t,j);formula,j=arg(t,j);assignment,end=bracket_arg(t,j)
            if assignment is not None:j=end
            repl=r'\mathfrak{'+structure+'}'+((','+assignment) if assignment is not None else '')+(r'\nvDash ' if neg else r'\vDash ')+formula
            t=t[:m.start()]+repl+t[j:];pos=m.start()+len(repl)
        return t
    def expand_value(t):
        pat=re.compile(r'\\Value(?![A-Za-z])');pos=0
        while (m:=pat.search(t,pos)):
            term,j=arg(t,m.end());structure,j=arg(t,j);assignment,end=bracket_arg(t,j)
            if assignment is not None:j=end
            repl=r'\mathrm{Val}^{\mathfrak{'+structure+'}}'+(('_{'+assignment+'}') if assignment is not None else '')+'('+term+')'
            t=t[:m.start()]+repl+t[j:];pos=m.start()+len(repl)
        return t
    body=expand_optional_command(body,'lforall',lambda _slash,a:r'\forall'+((' '+a[0]) if a else '')+((r' \, '+a[1]) if len(a)>1 else ''))
    body=expand_optional_command(body,'lexists',lambda unique,a:r'\exists'+('!' if unique else '')+((' '+a[0]) if a else '')+((r' \, '+a[1]) if len(a)>1 else ''))
    body=expand_optional_command(body,'eq',lambda neg,a:r'{}'+((a[0]+(r'\ne ' if neg else '=')+a[1]) if len(a)>1 else (r'\ne ' if neg else '=')))
    body=expand_sat(body)
    body=expand_value(body)
    body=command(body,'varAssign',3,lambda new,old,var:new+r'\sim_{'+var+'}'+old)
    body=body.replace(r'\Proves/',r'\nvdash').replace(r'\Entails/',r'\nvDash')
    body=command(body,'DischargeRule',2,lambda rule,index:
                 r'\RightLabel{'+rule+r',\,'+index+'}')

    class TableauNode:
        def __init__(self,formula='',children=(),just='',checked=False,closed=False,move=''):
            self.formula=formula.strip();self.children=list(children);self.just=just.strip()
            self.checked=checked;self.closed=closed;self.move=move.strip();self.number=None
    def split_tableau_fields(text):
        fields=[];start=0;braces=brackets=0
        for i,ch in enumerate(text):
            escaped=i>0 and text[i-1]=='\\'
            if ch=='{' and not escaped:braces+=1
            elif ch=='}' and not escaped:braces-=1
            elif ch=='[' and not escaped:brackets+=1
            elif ch==']' and not escaped:brackets-=1
            elif ch==',' and not braces and not brackets:
                fields.append(text[start:i].strip());start=i+1
        fields.append(text[start:].strip())
        assert braces==brackets==0,(braces,brackets,text[:120])
        return fields
    def strip_outer_group(text):
        text=text.strip()
        if not text.startswith('{'):return text
        value,end=arg(text,0)
        return value.strip() if end==len(text) else text
    def parse_tableau_node(text,pos=0):
        while pos<len(text) and text[pos].isspace():pos+=1
        assert pos<len(text) and text[pos]=='[',(pos,text[pos:pos+100])
        pos+=1;start=pos;header=[];children=[];braces=0
        while pos<len(text):
            ch=text[pos];escaped=pos>0 and text[pos-1]=='\\'
            if ch=='{' and not escaped:braces+=1;pos+=1;continue
            if ch=='}' and not escaped:braces-=1;assert braces>=0;pos+=1;continue
            if not braces and ch=='[':
                reference=re.match(r'\[\s*\d+(?:\s*,\s*\d+)*\s*\]',text[pos:])
                if reference:
                    pos+=reference.end();continue
                header.append(text[start:pos])
                child,pos=parse_tableau_node(text,pos);children.append(child);start=pos
                continue
            if not braces and ch==']':
                header.append(text[start:pos]);pos+=1;break
            pos+=1
        else:raise AssertionError(('unterminated tableau node',text[:160]))
        fields=split_tableau_fields(''.join(header))
        if len(fields)==1 and not fields[0]:return TableauNode(children=children),pos
        formula=fields[0];just='';checked=closed=False;move='';unknown=[]
        for option in fields[1:]:
            option=option.strip()
            if not option:continue
            if option=='checked':checked=True
            elif option=='close':closed=True
            elif re.match(r'just\s*=',option):just=strip_outer_group(option.split('=',1)[1])
            elif re.match(r'move by\s*=',option):move=option.split('=',1)[1].strip()
            else:unknown.append(option)
        assert not unknown,(unknown,formula)
        return TableauNode(formula,children,just,checked,closed,move),pos
    def tableau_stats(root):
        rows=[]
        def visit(node,depth):
            rows.append((node,depth))
            for child in node.children:visit(child,depth+1)
        visit(root,1)
        return dict(
            nodes=sum(bool(node.formula) for node,_ in rows),
            empty_branches=sum(not node.formula for node,_ in rows),
            edges=sum(len(node.children) for node,_ in rows),
            leaves=sum(not node.children for node,_ in rows),
            max_depth=max(depth for _,depth in rows),
            checked_nodes=sum(node.checked for node,_ in rows),
            closed_nodes=sum(node.closed for node,_ in rows),
            moved_nodes=sum(bool(node.move) for node,_ in rows),
        )
    def number_tableau(root,numbered):
        counter=0
        def visit(node):
            nonlocal counter
            if node.formula:
                counter+=1;node.number=counter if numbered else None
            for child in node.children:visit(child)
        visit(root)
        return counter
    def tableau_math(node):
        if not node.formula:
            return r'\phantom{\sFmla{\True}{\varphi}}'
        formula=node.formula.strip()
        if formula.startswith('$') and formula.endswith('$'):formula=formula[1:-1]
        if node.checked:formula+=r'\;{}^{\checkmark}'
        just=node.just.replace(r'\TAss',r'\text{ધારણા}').strip()
        if just.startswith('$') and just.endswith('$'):just=just[1:-1]
        if node.closed:just+=(r'\quad ' if just else '')+r'\times'
        number=(str(node.number)+'.') if node.number is not None else r'\phantom{0.}'
        just_cell=(r'{\scriptstyle '+just+'}') if just else '{}'
        line=r'\begin{array}{rcl}'+number+'&'+formula+'&'+just_cell+r'\end{array}'
        if not node.children:return line
        children=[tableau_math(child) for child in node.children]
        if len(children)==1:
            connector=r'\downarrow';lower=children[0]
        else:
            columns='c'*len(children)
            arrows=[r'\swarrow',r'\searrow'] if len(children)==2 else [r'\downarrow']*len(children)
            connector=r'\begin{array}{'+columns+'}'+'&'.join(arrows)+r'\end{array}'
            lower=r'\begin{array}{'+columns+'}'+'&'.join(children)+r'\end{array}'
        return r'\begin{array}{c}'+line+r'\\[-.35ex]'+connector+r'\\[-.35ex]'+lower+r'\end{array}'
    def tableau_region(source,payload,numbered,kind):
        payload=payload.lstrip()
        if payload.startswith('{'):
            options,end=arg(payload,0)
            assert not options.strip(),options
            payload=payload[end:]
        root,pos=parse_tableau_node(payload)
        assert not payload[pos:].strip(),payload[pos:pos+120]
        count=number_tableau(root,numbered);stats=tableau_stats(root)
        assert count==stats['nodes'] and count>0
        proof_render_receipts.append(dict(
            kind=kind,source_sha256=hashlib.sha256(source.encode('utf-8')).hexdigest(),
            numbered=numbered,**stats,
            representation='Recursive MathML signed-formula tree preserving node order, branch structure, justifications, checkmarks, closure marks and intentional empty branches.',
        ))
        return '\n\\['+tableau_math(root)+r'\]'+'\n'
    if edition in {'tableaux','axiomatic-deduction','completeness','first-order-introduction','first-order-syntax'}:
        body=re.sub(
            r'\\begin\{oltableau\}([\s\S]*?)\\end\{oltableau\}(?:\{\})?',
            lambda m:tableau_region(m[0],m[1],True,'signed_analytic_tableau'),body,
        )
        body=re.sub(
            r'\\begin\{tableau\}\{([^{}]*)\}([\s\S]*?)\\end\{tableau\}(?:\{\})?',
            lambda m:tableau_region(m[0],m[2],m[1].strip()!='not line numbering','signed_analytic_tableau'),body,
        )
        assert not re.search(r'\\begin\{(?:oltableau|tableau)\}',body)

    class ProofNode:
        def __init__(self,formula,children=(),label='',kind='axiom',double=False,empty=False):
            self.formula=formula.strip();self.children=list(children);self.label=label.strip()
            self.kind=kind;self.double=double;self.empty=empty
    def proof_math(node):
        if not node.children:
            return r'\phantom{\varphi}' if node.empty else node.formula
        if node.kind=='deduce' and node.children[0].empty:
            upper=r'\vdots'
        else:
            upper=(r'\qquad'.join(proof_math(child) for child in node.children))
        label=(r'\;'+node.label) if node.label else ''
        return r'\frac{'+upper+'}{'+node.formula+'}'+label
    def proof_region(source,kind):
        command_pat=re.compile(r'\\(AxiomC|Axiom|DeduceC|Deduce|UnaryInfC|UnaryInf|BinaryInfC|BinaryInf|TrinaryInfC|TrinaryInf|RightLabel|DisplayProof|bottomAlignProof|doubleLine|noLine|insertBetweenHyps|hfill|hspace|qquad|quad|noindent)(?![A-Za-z])')
        stack=[];trees=[];pending_label='';pending_double=False;pos=0
        counts={'axioms':0,'inferences':0,'deductions':0,'empty_premises':0,'double_lines':0}
        while (m:=command_pat.search(source,pos)):
            name=m[1];j=m.end()
            if name=='AxiomC':
                formula,j=arg(source,j);formula=formula.replace('$','');empty=not formula.strip();stack.append(ProofNode(formula,empty=empty))
                counts['axioms']+=1;counts['empty_premises']+=int(empty)
            elif name in {'Axiom','DeduceC','Deduce','UnaryInfC','UnaryInf','BinaryInfC','BinaryInf','TrinaryInfC','TrinaryInf'}:
                if name.endswith('C'):
                    formula,j=arg(source,j)
                    formula=formula.replace('$','')
                else:
                    while j<len(source) and source[j].isspace():j+=1
                    assert j<len(source) and source[j]=='$',(kind,name,source[j:j+80])
                    end=source.find('$',j+1);assert end!=-1
                    formula=source[j+1:end];j=end+1
                if name=='Axiom':
                    stack.append(ProofNode(formula));counts['axioms']+=1
                else:
                    arity=3 if name.startswith('TrinaryInf') else 2 if name.startswith('BinaryInf') else 1
                    assert len(stack)>=arity,(kind,name,len(stack),formula)
                    children=stack[-arity:];del stack[-arity:]
                    stack.append(ProofNode(formula,children,pending_label,'deduce' if name.startswith('Deduce') else 'inference',pending_double))
                    counts['inferences']+=1;counts['deductions']+=int(name.startswith('Deduce'))
                    counts['double_lines']+=int(pending_double);pending_label='';pending_double=False
            elif name=='RightLabel':
                pending_label,j=arg(source,j)
                if pending_label.startswith('$') and pending_label.endswith('$'):pending_label=pending_label[1:-1]
            elif name=='doubleLine':pending_double=True
            elif name in {'insertBetweenHyps','hspace'}:
                _,j=arg(source,j)
            elif name=='DisplayProof':
                assert len(stack)==1,(kind,'display',len(stack))
                trees.append(stack.pop())
            pos=j
        if stack:
            assert len(stack)==1,(kind,'end',len(stack));trees.append(stack.pop())
        assert trees,(kind,'no trees')
        rendered='\n'.join(r'\['+proof_math(tree)+r'\]' for tree in trees)
        proof_render_receipts.append(dict(
            kind=kind,source_sha256=hashlib.sha256(source.encode('utf-8')).hexdigest(),
            trees=len(trees),**counts,
            representation='Recursive MathML inference fractions preserving every premise, conclusion, branch and rule label; dotted omissions remain vertical dots and open premises remain visually blank.',
        ))
        return '\n'+rendered+'\n'
    def proof_kind(source,display):
        system='sequent' if r'\fCenter' in source else 'natural_deduction'
        return system+('_rule_display' if display else '_prooftree')
    body=re.sub(r'\\begin\{defish\}[\s\S]*?\\end\{defish\}',lambda m:proof_region(m[0],proof_kind(m[0],True)),body)
    body=re.sub(r'\\begin\{prooftree\}[\s\S]*?\\end\{prooftree\}',lambda m:proof_region(m[0],proof_kind(m[0],False)),body)
    assert not re.search(r'\\(?:AxiomC|Axiom|DeduceC|Deduce|UnaryInfC|UnaryInf|BinaryInfC|BinaryInf|TrinaryInfC|TrinaryInf|RightLabel|DisplayProof|DischargeRule)(?![A-Za-z])',body)
authors={'Cantor1892':'કૅન્ટૉર','Frege1884':'ફ્રેગે','Potter2004':'પૉટર',
         'Benacerraf1965':'બેનાસેરાફ','Conway2006':'કૉનવે',
         'KatzKatz2012':'કૅટ્ઝ અને કૅટ્ઝ',
         'OConnorRobertson:RN':"ઓ'કૉનર અને રૉબર્ટસન",
         'EwaldSieg2013':'હિલ્બર્ટ','Dedekind1888':'ડેડેકિન્ડ',
         'Magnus2021':'મૅગ્નસ અને અન્ય','Smullyan1968':'સ્મલ્યન',
         'Zuckerman1973':'ઝકરમૅન'}
years={'Cantor1892':'1892','Frege1884':'1884','Potter2004':'2004',
       'Benacerraf1965':'1965','Conway2006':'2006','KatzKatz2012':'2012',
       'OConnorRobertson:RN':'2005','EwaldSieg2013':'2013','Dedekind1888':'1888',
       'Magnus2021':'2021','Smullyan1968':'1968','Zuckerman1973':'1973'}
def citation_note(note):
    if not note:return ''
    note=' '.join(note.replace(r'\S','§').replace('~',' ').replace('--','–').split())
    return note.replace('Theorems','પ્રમેયો').replace('preface','પ્રસ્તાવના')
def textual_citation(match):
    note,key=match.groups();extra=', '+citation_note(note) if note else ''
    return r'\hyperref[bib:'+key+']{'+authors[key]+' ('+years[key]+extra+')} '
def parenthetical_citation(match):
    note,key=match.groups();extra=', '+citation_note(note) if note else ''
    return r'(\hyperref[bib:'+key+']{'+authors[key]+' '+years[key]+extra+'})'
body=re.sub(r'\\citet(?:\[([^\]]*)\])?\{([^}]+)\}',textual_citation,body)
body=re.sub(r'\\citep(?:\[([^\]]*)\])?\{([^}]+)\}',parenthetical_citation,body)
body=re.sub(r'\\citealt(?:\[([^\]]*)\])?\{([^}]+)\}',lambda m:r'\hyperref[bib:'+m[2]+']{'+authors[m[2]]+' '+years[m[2]]+(', '+citation_note(m[1]) if m[1] else '')+'}',body)
body=re.sub(r'\\citeyear(?:\[([^\]]*)\])?\{([^}]+)\}',lambda m:r'\hyperref[bib:'+m[2]+']{'+years[m[2]]+(', '+citation_note(m[1]) if m[1] else '')+'}',body)
body=re.sub(r'\\citeauthor\{([^}]+)\}',lambda m:r'\hyperref[bib:'+m[1]+']{'+authors[m[1]]+'}',body)
body=re.sub(r'\\cite\{([^}]+)\}',lambda m:'('+r'\hyperref[bib:'+m[1]+']{'+authors[m[1]]+' '+years[m[1]]+'})',body)
body=body.replace(r'\textparagraph','¶')
body=command(body,'part',1,lambda x:'') # Chapter identity appears in grouped introduction; section numbering continuous.
# Pandoc's LaTeX math reader cannot retain a hyperlink nested inside a
# Gujarati \text{...} alignment cell.  The displayed proof already carries
# the surrounding explanatory text, so keep the verified proposition number
# as plain math text in this one source citation.
body=body.replace(r'\hyperref[fol:com:ide:lem:val-in-termmodel-factored]{116.6}', '116.6')
graph_receipts=[];graph_alt={}
def render_graph(m):
    src=m[0]
    if r'\foreach \x in {1, 2, 3, 4, 5, 6, 7, 8, 9}' in src:
        arrows=re.findall(r'\\draw\[->\] \((\d)b\)--\((\d)a\);',src)
        assert arrows==[(str(i),str(i+1)) for i in range(1,9)] and r'\draw[->] (9b)--(dotsa);' in src
        name='hilbert-hotel-shift'
        alt='ઉપરની હારમાં જૂના મહેમાનો 1થી 9 અને આગળ; દરેક તીર મહેમાન nને નીચેની હારમાં ઓરડા n+1માં ખસેડે છે. નીચેનો ઓરડો 1 વર્તુળથી ખાલી દર્શાવ્યો છે.'
        svg=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 190" role="img"><defs><marker id="hotel-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="none" stroke="#222"/></marker></defs>']
        for i in range(1,10):
            x=50+70*(i-1)
            svg.append(f'<text x="{x}" y="42" text-anchor="middle" font-family="serif" font-size="21">{i}</text>')
            svg.append(f'<text x="{x}" y="157" text-anchor="middle" font-family="serif" font-size="21">{i}</text>')
        svg.append('<text x="690" y="42" text-anchor="middle" font-family="serif" font-size="24">…</text><text x="690" y="157" text-anchor="middle" font-family="serif" font-size="24">…</text>')
        for i in range(1,9):
            x1=50+70*(i-1);x2=50+70*i
            svg.append(f'<path d="M{x1},54 L{x2},132" fill="none" stroke="#222" stroke-width="1.8" marker-end="url(#hotel-arrow)"/>')
        svg.append('<path d="M610,54 L680,132" fill="none" stroke="#222" stroke-width="1.8" marker-end="url(#hotel-arrow)"/><circle cx="50" cy="151" r="27" fill="none" stroke="#222" stroke-width="2"/></svg>')
        path=O/'assets'/f'{name}.svg';path.write_text(''.join(svg),encoding='utf-8',newline='\n')
        graph_receipts.append(dict(asset=path.relative_to(R).as_posix(),source_tikz_sha256=hashlib.sha256(src.encode('utf-8')).hexdigest(),svg_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),rooms=list(range(1,10)),arrows=[(i,i+1) for i in range(1,10)],method='Deterministic SVG reconstruction of the validated Hilbert Hotel labels, shift arrows and circled vacant room 1.'))
        graph_alt[name]=alt
        return '\n\n'+r'\includegraphics{assets/'+name+'.svg}\n\n'
    if 'fill=red!50' in src and 'rectangle (2.3,2.3)' in src:
        name='sqrt-two-parity'
        alt='બાજુ mવાળો મોટો ચોરસ; તેની અંદર બાજુ nવાળા બે સરખા, એકબીજા પર ચઢતા ચોરસ. નારંગી છેદનું ક્ષેત્રફળ બંને ઢાંકાયા વિનાના ખૂણાના ચોરસોના કુલ ક્ષેત્રફળ જેટલું છે.'
        svg='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 470 290" role="img"><defs><marker id="both" markerWidth="7" markerHeight="7" refX="3.5" refY="3.5" orient="auto-start-reverse"><path d="M0,0 L7,3.5 L0,7" fill="none" stroke="#222"/></marker></defs><rect x="40" y="20" width="240" height="240" fill="white" stroke="#222" stroke-width="2.5"/><rect x="40" y="76" width="184" height="184" fill="#ef9a9a" stroke="#222" stroke-width="2.5"/><rect x="96" y="20" width="184" height="184" fill="#fff59d" stroke="#222" stroke-width="2.5"/><rect x="96" y="76" width="128" height="128" fill="#ffb74d" stroke="#222" stroke-width="2.5"/><path d="M340,20 L340,204" stroke="#222" stroke-width="1.8" marker-start="url(#both)" marker-end="url(#both)"/><text x="361" y="118" font-family="serif" font-size="20">n</text><path d="M410,20 L410,260" stroke="#222" stroke-width="1.8" marker-start="url(#both)" marker-end="url(#both)"/><text x="431" y="146" font-family="serif" font-size="20">m</text></svg>'''
        path=O/'assets'/f'{name}.svg';path.write_text(svg,encoding='utf-8')
        graph_receipts.append(dict(asset=path.relative_to(R).as_posix(),source_tikz_sha256=hashlib.sha256(src.encode('utf-8')).hexdigest(),svg_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),method='Deterministic SVG reconstruction of the validated four source rectangles and the n/m dimension arrows.'))
        graph_alt[name]=alt
        return '\n\n'+r'\includegraphics{assets/'+name+'.svg}\n\n'
    if '[grow\'=up]' in src:
        labels=re.findall(r'node\s*\{\$([^$]+)\$\}',src)
        root=re.search(r'\\node\{\$([^$]+)\$\}',src)[1]
        assert root=='r' and labels==['r','a','c','d','e','b']
        positions={'r':(210,215),'a':(145,130),'b':(280,130),'c':(65,45),'d':(145,45),'e':(225,45)}
        edges=[('r','a'),('r','b'),('a','c'),('a','d'),('a','e')]
        name='tree';directed=False
        alt='મૂળ rથી સંતાન a અને b; aનાં સંતાન c, d અને e. મૂળ નીચે અને સંતાનો ઉપર છે.'
    else:
        labels=re.findall(r'\\node\[draw,circle\]\s*\(([A-D])\)[^;]*\{\$([1-4])\$\};',src)
        expected=[('A','1'),('B','2'),('C','3')]
        assert labels in (expected,expected+[('D','4')])
        assert re.findall(r'\\draw \(([A-D])\) to\s*\(([A-D])\);',src)==[('A','B'),('A','C'),('B','C')]
        assert r'\draw (A) to [loop above]  (A);' in src
        pos={'1':(70,80),'2':(180,80),'3':(180,185),'4':(290,80)}
        positions={label:pos[label] for _,label in labels}
        edges=[('1','1'),('1','2'),('1','3'),('2','3')]
        name='graph-four' if len(labels)==4 else 'graph-three';directed=True
        alt='દિશાયુક્ત આલેખ: 1થી 1, 2 અને 3 તરફ ધારો; 2થી 3 તરફ ધાર.'+(' 4 છૂટું શિરોબિંદુ છે.' if len(labels)==4 else '')
    svg=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 350 260"><defs><marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="none" stroke="#222"/></marker></defs>']
    for a,b in edges:
        x,y=positions[a];xx,yy=positions[b]
        if a==b:
            d=f'M{x-11},{y-11} C{x-40},{y-65} {x+40},{y-65} {x+11},{y-11}'
        else:
            import math
            dx,dy=xx-x,yy-y;ln=math.hypot(dx,dy)
            x+=dx/ln*18;y+=dy/ln*18;xx-=dx/ln*20;yy-=dy/ln*20
            d=f'M{x:.3f},{y:.3f} L{xx:.3f},{yy:.3f}'
        svg.append(f'<path d="{d}" fill="none" stroke="#222" stroke-width="1.5"'+(' marker-end="url(#arrow)"' if directed else '')+'/>')
    for label,(x,y) in positions.items():
        svg.append(f'<circle cx="{x}" cy="{y}" r="17" fill="white" stroke="#222"/><text x="{x}" y="{y+5}" text-anchor="middle" font-family="serif" font-size="17">{label}</text>')
    svg.append('</svg>')
    path=O/'assets'/f'{name}.svg';path.write_text(''.join(svg),encoding='utf-8')
    graph_receipts.append(dict(asset=path.relative_to(R).as_posix(),source_tikz_sha256=hashlib.sha256(src.encode('utf-8')).hexdigest(),svg_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),vertices=list(positions),edges=edges,directed=directed,method='Deterministic SVG graph from validated original TikZ vertices and incidence. Layout computed for accessibility; mathematical incidence preserved.'))
    graph_alt[name]=alt
    return '\n\n'+r'\includegraphics{assets/'+name+'.svg}\n\n'
# Only graph-containing align environments are dismantled for images/intertext; ordinary math remains.
def align_graph(m):
    if r'\begin{tikzpicture}' not in m[0]:return m[0]
    t=m[0].replace(r'\begin{align*}','').replace(r'\end{align*}','')
    t=re.sub(r'(?m)^\s*&\s*','',t)
    return command(t,'intertext',1,lambda x:'\n\n'+x+'\n\n')
body=re.sub(r'\\begin\{align\*\}[\s\S]*?\\end\{align\*\}',align_graph,body)
body=re.sub(r'\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\}',render_graph,body)
def clean_align(m):
    src=re.sub(r'\\emph\{([^{}]*)\}',r'\\text{\1}',m[0])
    if r'\intertext' not in src:return src
    content=src[len(r'\begin{align*}'):-len(r'\end{align*}')]
    rendered=[];pos=0;pat=re.compile(r'\\intertext(?![A-Za-z])')
    while (hit:=pat.search(content,pos)):
        prose,end=arg(content,hit.end())
        before=content[pos:hit.start()].strip()
        if before:rendered.append(r'\begin{align*}'+before+r'\end{align*}')
        rendered.append('\n\n'+prose+'\n\n')
        pos=end
    after=content[pos:].strip()
    if after:rendered.append(r'\begin{align*}'+after+r'\end{align*}')
    return '\n'.join(rendered)
body=re.sub(r'\\begin\{align\*\}[\s\S]*?\\end\{align\*\}',clean_align,body)
# TexMath does not accept presentation-only size commands or outer-spacing
# column modifiers inside display arrays; neither carries mathematical content.
body=re.sub(r'(\\\[)\s*\\small\b',r'\1',body)
body=re.sub(r'\\begin\{array\}\{@\{\}([^}]*)@\{\}\}',r'\\begin{array}{\1}',body)
sections=re.split(r'(?=\\olfileid)',body);labels={};section_text=[];figcount=0
names={'defn':'વ્યાખ્યા','ex':'ઉદાહરણ','thm':'પ્રમેય','lem':'લેમા','prop':'વિધાન','cor':'ઉપસિદ્ધાંત','prob':'સ્વાધ્યાય','proof':'સાબિતી'}
for block in sections:
    if not block.strip():continue
    ident=re.search(r'\\olfileid\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}',block);prefix=':'.join(ident.groups())
    num=len(section_text)+1;count=probcount=0
    labels[prefix+':sec']=str(num)
    block=command(block,'olfileid',3,lambda a,b,c:'')
    block=re.sub(r'\\olsection\[[^\]]*\](?=\{)',r'\\olsection',block)
    block=command(block,'olsection',1,lambda title:r'\section{'+title+r'}\label{'+prefix+':sec}')
    block=re.sub(r'\\begin\{tagblock\}\{[^}]+\}|\\end\{tagblock\}','',block)
    block=re.sub(r'\\(?:begin|end)\{(?:explain|digress|intro)\}','',block)
    block=block.replace(r'\begin{editorial}',r'\begin{quote}\textbf{સંપાદકીય નોંધ.} ')
    block=block.replace(r'\end{editorial}',r'\end{quote}')
    block=block.replace(r'\begin{history}',r'\begin{quote}\textbf{ઇતિહાસ.} ')
    block=block.replace(r'\end{history}',r'\end{quote}')
    # Treat environment opening and all subsequent labels in display order.
    pat=re.compile(r'\\begin\{(defn|ex|thm|lem|prop|cor|prob|proof)\}(?:\[((?:[^\[\]]|\[[^\[\]]*\])*)\])?|\\(ollabel|label)\{([^}]+)\}')
    last='';out='';start=0
    for m in pat.finditer(block):
        out+=block[start:m.start()]
        typ,env_title,labelkind,label=m.groups()
        if label:
            full_label=prefix+':'+label if labelkind=='ollabel' else label
            if not (labelkind=='label' and full_label in labels and not last):
                labels[full_label]=last
            out+=r'\label{'+full_label+'}'
        else:
            if typ=='prob':probcount+=1;last=f'{num}.{probcount}'
            elif typ=='proof':last=''
            else:count+=1;last=f'{num}.{count}'
            out+=r'\begin{quote}\textbf{'+names[typ]+(' '+last if last else '')+(' ('+env_title+')' if env_title else '')+'.} '
        start=m.end()
    block=out+block[start:]
    block=re.sub(r'\\end\{(?:defn|ex|thm|lem|prop|cor|prob|proof)\}',r'\\end{quote}',block)
    def figure(m):
        global figcount
        figcount+=1;t=m[1];asset=re.search(r'\\olasset(?:\[[^\]]*\])?\{assets/diagrams/([^}]+)\.tikz\}',t)[1]
        cap,_=arg(t,re.search(r'\\caption',t).end())
        lid=re.search(r'\\label\{([^}]+)\}',t)[1];labels[lid]=str(figcount)
        return r'\begin{center}\includegraphics{assets/'+asset+r'.svg}'+'\n'+r'\textbf{આકૃતિ '+str(figcount)+'.} '+cap+r'\label{'+lid+r'}\end{center}'
    block=re.sub(r'\\begin\{figure\}([\s\S]*?)\\end\{figure\}',figure,block)
    section_text.append((prefix,block))
# This label marks the third item in Dedekind's displayed three-condition list.
labels['sfr:infinite:dedekind:repeatedapplication']='3'
texts=[]
for prefix,block in section_text:
    def ref(m):
        opts=re.findall(r'\[([^\]]*)\]',m[1]);key=m[2]
        base=prefix.split(':')
        lid=':'.join(base[:3-len(opts)]+opts+[key])
        if lid in labels and labels[lid]:
            return r'\hyperref['+lid+']{'+labels[lid]+'}'
        external={
            'mth:ind:idf:sec':('https://github.com/OpenLogicProject/OpenLogic/blob/9620cc73f9c8e0ad003c514a5d3748f29611c4c0/content/methods/induction/inductive-definitions.tex','મૂળ ગ્રંથનો અનુમાનાત્મક વ્યાખ્યાઓ અંગેનો વિભાગ'),
            'mth:ind:sti:sec':('https://github.com/OpenLogicProject/OpenLogic/blob/9620cc73f9c8e0ad003c514a5d3748f29611c4c0/content/methods/induction/structural-induction.tex','મૂળ ગ્રંથનો રચના પરના અનુમાન અંગેનો વિભાગ'),
            'his:set:limits:sec':('https://github.com/OpenLogicProject/OpenLogic/blob/9620cc73f9c8e0ad003c514a5d3748f29611c4c0/content/history/set-theory/limits.tex','મૂળ ગ્રંથનો લક્ષોનો વિભાગ'),
            'his:set:mythology:sec':('https://github.com/OpenLogicProject/OpenLogic/blob/9620cc73f9c8e0ad003c514a5d3748f29611c4c0/content/history/set-theory/mythology.tex','મૂળ ગ્રંથનો સંબંધિત ઐતિહાસિક વિભાગ'),
            'sth:::part':('https://github.com/OpenLogicProject/OpenLogic/tree/9620cc73f9c8e0ad003c514a5d3748f29611c4c0/content/set-theory','મૂળ ગ્રંથનો ગણસિદ્ધાંત ભાગ'),
            'sth:ord-arithmetic::chap':('https://github.com/OpenLogicProject/OpenLogic/tree/9620cc73f9c8e0ad003c514a5d3748f29611c4c0/content/set-theory/ord-arithmetic','મૂળ ગ્રંથનું ક્રમસંખ્યાઓના અંકગણિતનું પ્રકરણ'),
            'fol:syn:sem:prop:quant-terms':('https://github.com/OpenLogicProject/OpenLogic/blob/9620cc73f9c8e0ad003c514a5d3748f29611c4c0/content/first-order-logic/syntax-and-semantics/semantic-notions.tex','મૂળ ગ્રંથનું પરિમાણક અને પદ અંગેનું વિધાન'),
            'fol:syn:sem:thm:sem-deduction':('https://github.com/OpenLogicProject/OpenLogic/blob/9620cc73f9c8e0ad003c514a5d3748f29611c4c0/content/first-order-logic/syntax-and-semantics/semantic-notions.tex','મૂળ ગ્રંથનું અર્થવિચારી નિગમન પ્રમેય'),
            'fol:syn:ass:prop:sat-quant':('https://github.com/OpenLogicProject/OpenLogic/blob/9620cc73f9c8e0ad003c514a5d3748f29611c4c0/content/first-order-logic/syntax-and-semantics/assignments.tex','મૂળ ગ્રંથનું પરિમાણક-સંતોષ અંગેનું વિધાન'),
            'fol:syn:ass:prop:sentence-sat-true':('https://github.com/OpenLogicProject/OpenLogic/blob/9620cc73f9c8e0ad003c514a5d3748f29611c4c0/content/first-order-logic/syntax-and-semantics/assignments.tex','મૂળ ગ્રંથનું વાક્યના સંતોષ અંગેનું વિધાન'),
            'fol:syn:sat:defn:satisfaction':('https://github.com/OpenLogicProject/OpenLogic/blob/9620cc73f9c8e0ad003c514a5d3748f29611c4c0/content/first-order-logic/syntax-and-semantics/satisfaction.tex','મૂળ ગ્રંથની સંતોષ અંગેની વ્યાખ્યા'),
            'fol:syn:ext:cor:extensionality-sent':('https://github.com/OpenLogicProject/OpenLogic/blob/9620cc73f9c8e0ad003c514a5d3748f29611c4c0/content/first-order-logic/syntax-and-semantics/extensionality.tex','મૂળ ગ્રંથનું વાક્યની વિસ્તરણાત્મકતા અંગેનું ઉપસિદ્ધાંત'),
            'fol:syn:ext:prop:ext-formulas':('https://github.com/OpenLogicProject/OpenLogic/blob/9620cc73f9c8e0ad003c514a5d3748f29611c4c0/content/first-order-logic/syntax-and-semantics/extensionality.tex','મૂળ ગ્રંથનું સૂત્રોની વિસ્તરણાત્મકતા અંગેનું વિધાન'),
            'fol:syn:ext:prop:extensionality':('https://github.com/OpenLogicProject/OpenLogic/blob/9620cc73f9c8e0ad003c514a5d3748f29611c4c0/content/first-order-logic/syntax-and-semantics/extensionality.tex','મૂળ ગ્રંથનું વિસ્તરણાત્મકતા અંગેનું વિધાન'),
            'fol:syn:sem:prop:entails-unsat':('https://github.com/OpenLogicProject/OpenLogic/blob/9620cc73f9c8e0ad003c514a5d3748f29611c4c0/content/first-order-logic/syntax-and-semantics/semantic-notions.tex','મૂળ ગ્રંથનું અસંતોષ્યતા અને અર્થાનુસરણ અંગેનું વિધાન'),
        }
        if lid in external:
            url,text=external[lid]
            return r'\href{'+url+'}{'+text+'}'
        if lid=='sfr:siz::chap' and 'sfr:siz:int:sec' in labels:
            return r'\hyperref[sfr:siz:int:sec]{ગણોના કદનું પ્રકરણ}'
        if lid=='sfr:arith::chap' and 'sfr:arith:int:sec' in labels:
            return r'\hyperref[sfr:arith:int:sec]{અંકગણિતીકરણનું પ્રકરણ}'
        raise AssertionError(lid)
    block=re.sub(r'\\olref((?:\[[^\]]*\])*)\{([^}]+)\}',ref,block)
    block=block.replace(r'\hyperref[fol:com:ide:lem:val-in-termmodel-factored]{116.6}', '116.6')
    def cref(m):
        lid=m[1]
        assert lid in labels and labels[lid],lid
        return r'\hyperref['+lid+']{'+labels[lid]+'}'
    block=re.sub(r'\\cref\{([^}]+)\}',cref,block)
    block=block.replace(r'\begin{multline*}',r'\[\begin{aligned}').replace(r'\end{multline*}',r'\end{aligned}\]')
    block=command(block,'shoveright',1,lambda x:x);block=command(block,'shoveleft',1,lambda x:x)
    texts.append(block)
# The first-release HTML preparation retains its independently verified exact-path set diagrams.
for name in ('union','intersection','difference'):assert (O/'assets'/f'{name}.svg').exists()
macros=r"""
\newcommand{\Nat}{\mathbb{N}}
\newcommand{\Int}{\mathbb{Z}}
\newcommand{\Rat}{\mathbb{Q}}
\newcommand{\Real}{\mathbb{R}}
\newcommand{\PosInt}{\mathbb{Z}^+}
\newcommand{\Bin}{\mathbb{B}}
\newcommand{\Pow}[1]{\wp(#1)}
\newcommand{\Setabs}[2]{\{#1:#2\}}
\newcommand{\tuple}[1]{\langle#1\rangle}
\newcommand{\len}[1]{\mathrm{len}(#1)}
\newcommand{\lif}{\rightarrow}
\newcommand{\liff}{\leftrightarrow}
\newcommand{\defis}{\mathrel{:=}}
\newcommand{\phi}{\varphi}
\newcommand{\nicefrac}[2]{\frac{#1}{#2}}
\newcommand{\Id}[1]{\mathrm{Id}_{#1}}
\newcommand{\equivrep}[2]{[#1]_{#2}}
\newcommand{\equivclass}[2]{#1/_{\!{#2}}}
\newcommand{\Intequiv}{\mathrel{\sim_{\Int}}}
\newcommand{\Ratequiv}{\mathrel{\sim_{\Rat}}}
\newcommand{\Realequiv}{\mathrel{\sim_{\Real}}}
\newcommand{\funrestrictionto}[2]{#1\mathord{\restriction}_{#2}}
\newcommand{\funimage}[2]{#1[#2]}
\newcommand{\emptyseq}{\Lambda}
\newcommand{\dom}[1]{\mathrm{dom}(#1)}
\newcommand{\ran}[1]{\mathrm{ran}(#1)}
\newcommand{\Domain}[1]{\mathrm{dom}(#1)}
\newcommand{\Trm}[1]{\mathrm{Trm}(#1)}
\newcommand{\num}[1]{\overline{#1}}
\newcommand{\comp}[2]{#2\circ #1}
\newcommand{\cardeq}[2]{\lvert#1\rvert=\lvert#2\rvert}
\newcommand{\cardneq}[2]{\lvert#1\rvert\ne\lvert#2\rvert}
\newcommand{\cardle}[2]{\lvert#1\rvert\le\lvert#2\rvert}
\newcommand{\cardless}[2]{\lvert#1\rvert<\lvert#2\rvert}
\newcommand{\funfromto}[2]{#2^{#1}}
\newcommand{\closureofunder}[2]{\mathrm{clo}_{#1}(#2)}
\newcommand{\Closureofunder}[2]{\mathrm{Clo}_{#1}(#2)}
\newcommand{\pto}{\mathrel{\text{GU-PARTIAL-ARROW}}}
\newcommand{\fdefined}{\downarrow}
\newcommand{\fundefined}{\uparrow}
\newcommand{\True}{\mathbb{T}}
\newcommand{\False}{\mathbb{F}}
\newcommand{\lfalse}{\bot}
\newcommand{\ltrue}{\top}
\newcommand{\Obj}[1]{\mathsf{#1}}
\newcommand{\Lang}[1]{\mathcal{#1}}
\newcommand{\Log}[1]{\mathbf{#1}}
\newcommand{\Frm}[1][]{\mathrm{Frm}(\mathcal{#1})}
\newcommand{\PVar}{\mathrm{At}_0}
\newcommand{\Struct}[1]{\mathfrak{#1}}
\newcommand{\Atom}[2]{#1(#2)}
\newcommand{\Assign}[2]{#1^{\mathfrak{#2}}}
\newcommand{\pAssign}[1]{\mathfrak{#1}}
\newcommand{\pValue}[1]{\overline{\mathfrak{#1}}}
\newcommand{\Entails}{\vDash}
\newcommand{\ident}{\equiv}
\newcommand{\subst}[2]{#1/#2}
\newcommand{\SSubst}[2]{#1[#2]}
\newcommand{\Subst}[3]{#1[#2/#3]}
\newcommand{\Proves}{\vdash}
\newcommand{\Sequent}{\Rightarrow}
\newcommand{\fCenter}{\Sequent}
\newcommand{\LeftR}[1]{#1\mathrm{L}}
\newcommand{\RightR}[1]{#1\mathrm{R}}
\newcommand{\Weakening}{\mathrm{W}}
\newcommand{\Contraction}{\mathrm{C}}
\newcommand{\Exchange}{\mathrm{X}}
\newcommand{\Cut}{\mathrm{Cut}}
\newcommand{\Intro}[1]{#1\mathrm{Intro}}
\newcommand{\Elim}[1]{#1\mathrm{Elim}}
\newcommand{\FalseInt}{\bot_I}
\newcommand{\FalseCl}{\bot_C}
\newcommand{\Discharge}[2]{[#1]^{#2}}
\newcommand{\sFmla}[2]{#1\,#2}
\newcommand{\TRule}[2]{#2#1}
\newcommand{\formula}[1]{#1}
\newcommand{\MP}{\mathrm{MP}}
\newcommand{\QR}{\mathrm{QR}}
\newcommand{\Hyp}{\text{પૂર્વધારણા}}
\newcommand{\PAx}{\mathrm{Ax}_0}
"""
editorial_path=(R/'gu-tableaux.tex') if edition in {'axiomatic-deduction','completeness','first-order-introduction','first-order-syntax'} else (R/f'gu-{edition}.tex')
editorial=editorial_path.read_text(encoding='utf-8').split(r'\section*{સંપાદકીય નોંધો}',1)[1].split(r'\begin{thebibliography}',1)[0]
if edition in {'tableaux','axiomatic-deduction','completeness','first-order-introduction','first-order-syntax'}:
    correction_ids={
        'tableaux':('OLFUN-001થી OLFUN-005, OLSIZ-001થી OLSIZ-012, '
                    'OLARI-001થી OLARI-004, OLINF-001થી OLINF-002, '
                    'OLPL-001થી OLPL-002, OLPRF-001થી OLPRF-004, '
                    'OLSEQ-001થી OLSEQ-006, OLND-001થી OLND-006 અને '
                    'OLTAB-001થી OLTAB-012 સુધીની'),
        'axiomatic-deduction':('OLFUN-001થી OLFUN-005, OLSIZ-001થી OLSIZ-012, '
                    'OLARI-001થી OLARI-004, OLINF-001થી OLINF-002, '
                    'OLPL-001થી OLPL-002, OLPRF-001થી OLPRF-004, '
                    'OLSEQ-001થી OLSEQ-006, OLND-001થી OLND-006, '
                    'OLTAB-001થી OLTAB-012 અને OLAX-001થી OLAX-018 સુધીની'),
        'completeness':('OLFUN-001થી OLFUN-005, OLSIZ-001થી OLSIZ-012, '
                    'OLARI-001થી OLARI-004, OLINF-001થી OLINF-002, '
                    'OLPL-001થી OLPL-002, OLPRF-001થી OLPRF-004, '
                    'OLSEQ-001થી OLSEQ-006, OLND-001થી OLND-006, '
                    'OLTAB-001થી OLTAB-012, OLAX-001થી OLAX-018 અને '
                    'OLCO-001થી OLCO-022 સુધીની'),
        'first-order-introduction':('OLFUN-001થી OLFUN-005, OLSIZ-001થી OLSIZ-012, '
                    'OLARI-001થી OLARI-004, OLINF-001થી OLINF-002, '
                    'OLPL-001થી OLPL-002, OLPRF-001થી OLPRF-004, '
                    'OLSEQ-001થી OLSEQ-006, OLND-001થી OLND-006, '
                    'OLTAB-001થી OLTAB-012, OLAX-001થી OLAX-018, '
                    'OLCO-001થી OLCO-022 અને OLFINT-001થી OLFINT-006 સુધીની'),
        'first-order-syntax':('OLFUN-001થી OLFUN-005, OLSIZ-001થી OLSIZ-012, '
                    'OLARI-001થી OLARI-004, OLINF-001થી OLINF-002, '
                    'OLPL-001થી OLPL-002, OLPRF-001થી OLPRF-004, '
                    'OLSEQ-001થી OLSEQ-006, OLND-001થી OLND-006, '
                    'OLTAB-001થી OLTAB-012, OLAX-001થી OLAX-018, '
                    'OLCO-001થી OLCO-022, OLFINT-001થી OLFINT-006 અને '
                    'OLSYN-001થી OLSYN-007 સુધીની'),
    }[edition]
    latest_editorial={
        'tableaux':('ટેબ્લોના નવા પ્રકરણમાં સ્થિર મૂળની શાસ્ત્રીય પ્રથમ-ક્રમ '
                    'ગોઠવણી પસંદ કરી છે. તેથી વિધાનાત્મક અને પરિમાણક નિયમો, '
                    'આઇગનચલ-શરત, કટ નિયમ અને તાદાત્મ્ય સામેલ છે. ટેબ્લો, '
                    'ચિહ્નિત સૂત્ર અને આઇગનચલ માટેનાં ગુજરાતી રૂપો કામચલાઉ '
                    'છે અને નિષ્ણાત ચકાસણી માટે ચિહ્નિત છે.'),
        'axiomatic-deduction':('સ્વયંસિદ્ધિમૂલક નિષ્પત્તિના નવા પ્રકરણમાં સ્થિર '
                    'મૂળની શાસ્ત્રીય પ્રથમ-ક્રમ ગોઠવણી પસંદ કરી છે. તેથી '
                    'વિધાનાત્મક અને પરિમાણક સ્વયંસિદ્ધિઓ, મોડસ પોનેન્સ, '
                    'પરિમાણક-નિયમ અને તાદાત્મ્ય સામેલ છે. નિગમન પ્રમેય અને '
                    'સાબિતી-સૈદ્ધાંતિક ગુણધર્મોની ચર્ચામાં મૂળ પાઠની અઢાર '
                    'ઓળખેલી ખામીઓ પારદર્શક નોંધો સાથે મર્યાદિત રીતે સુધારી છે.'),
        'completeness':('પૂર્ણતાના નવા પ્રકરણમાં સ્થિર મૂળની શાસ્ત્રીય પ્રથમ-ક્રમ '
                    'ગોઠવણી પસંદ કરી છે. પૂર્ણતા પ્રમેયના બંને નિરૂપણ, હેન્કિન અને '
                    'લિન્ડનબાઉમ રચનાઓ, પદ-નિદર્શ, તાદાત્મ્ય માટેનું ભાગફલન, સઘનતા '
                    'અને લેવેનહાઇમ--સ્કોલેમ પ્રમેય સામેલ છે. મૂળ પાઠની બાવીસ '
                    'ઓળખેલી ખામીઓ પારદર્શક નોંધો સાથે મર્યાદિત રીતે સુધારી છે.'),
        'first-order-introduction':('નવા પરિચય-પ્રકરણમાં સ્થિર મૂળની શાસ્ત્રીય '
                    'પ્રથમ-ક્રમ ગોઠવણી પસંદ કરી છે. સૂત્રોની અનુમાનાત્મક રચના, '
                    'ચલ-નિયુક્તિ સાથેનો સંતોષ, પરિમાણકનો વ્યાપ, પ્રતિસ્થાપન, '
                    'નિદર્શસિદ્ધાંત અને યથાર્થતા--પૂર્ણતાની બંને દિશાઓ સામેલ છે. '
                    'મૂળ પાઠની છ ઓળખેલી ઔપચારિક અને અર્થલક્ષી ખામીઓ પારદર્શક '
                    'નોંધો સાથે મર્યાદિત રીતે સુધારી છે.'),
        'first-order-syntax':('નવા વાક્યરચના-પ્રકરણમાં સ્થિર મૂળની શાસ્ત્રીય '
                    'પ્રથમ-ક્રમ ગોઠવણી પસંદ કરી છે. પદો અને સૂત્રોની અનુમાનાત્મક '
                    'રચના, એકમાત્ર વાચનીયતા, મુખ્ય કારક, ઉપસૂત્રો, રચના-શ્રેણીઓ, '
                    'પરિમાણકનો વ્યાપ અને પકડ ટાળતું પ્રતિસ્થાપન સામેલ છે. મૂળ '
                    'પાઠની સાત ઓળખેલી ઔપચારિક ખામીઓ પારદર્શક નોંધો સાથે '
                    'મર્યાદિત રીતે સુધારી છે.'),
    }[edition]
    editorial=editorial.replace(r'\gueditioncorrectionids{}',correction_ids)
    editorial=editorial.replace(r'\gueditioneditorial',latest_editorial)
editorial=re.sub(r'\\addcontentsline\{toc\}\{section\}\{[^}]+\}','',editorial)
bibliography=(r'\section*{સંદર્ભગ્રંથો}\label{bib:Benacerraf1965}'+'\nBenacerraf, Paul. 1965. '+r'\emph{What numbers could not be}'+'. The Philosophical Review 74(1), 47–73.\n')
if edition=='size':
    bibliography += (r'\label{bib:Cantor1892}Cantor, Georg. 1892. Über eine elementare Frage der Mannigfaltigkeitslehre.'+'\n'
                     +r'\label{bib:Frege1884}Frege, Gottlob. 1884. \emph{Die Grundlagen der Arithmetik}.'+'\n'
                     +r'\label{bib:Potter2004}Potter, Michael. 2004. \emph{Set Theory and Its Philosophy}.'+'\n')
if edition in {'arithmetization','infinite','propositional','proof-systems','sequent-calculus','natural-deduction','tableaux','axiomatic-deduction','completeness','first-order-introduction','first-order-syntax'}:
    bibliography += (r'\label{bib:Cantor1892}Cantor, Georg. 1892. Über eine elementare Frage der Mannigfaltigkeitslehre.'+'\n'
                     +r'\label{bib:Frege1884}Frege, Gottlob. 1884. \emph{Die Grundlagen der Arithmetik}.'+'\n'
                     +r'\label{bib:Potter2004}Potter, Michael. 2004. \emph{Set Theory and Its Philosophy}.'+'\n'
                     +r'\label{bib:Conway2006}Conway, John. 2006. \emph{The Power of Mathematics}.'+'\n'
                     +r'\label{bib:KatzKatz2012}Katz, Karin Usadi and Mikhail G. Katz. 2012. Stevin Numbers and Reality.'+'\n'
                     +r"\label{bib:OConnorRobertson:RN}O'Connor, John J. and Edmund F. Robertson. 2005. The real numbers: Stevin to Hilbert."+'\n')
if edition in {'infinite','propositional','proof-systems','sequent-calculus','natural-deduction','tableaux','axiomatic-deduction','completeness','first-order-introduction','first-order-syntax'}:
    bibliography += (r'\label{bib:EwaldSieg2013}Hilbert, David. 2013. On the infinite. In \emph{David Hilbert’s Lectures on the Foundations of Arithmetic and Logic 1917–1933}.'+'\n'
                     +r'\label{bib:Dedekind1888}Dedekind, Richard. 1888. \emph{Was sind und was sollen die Zahlen?}.'+'\n')
if edition in {'first-order-introduction','first-order-syntax'}:
    bibliography += (r'\label{bib:Magnus2021}Magnus, P. D., Tim Button, J. Robert Loftis, Aaron Thomas-Bolduc, Robert Trueman, and Richard Zach. 2021. \emph{forall x: Calgary: An Introduction to Formal Logic}. F21 ed. Open Logic Project.'+'\n')
if edition == 'first-order-syntax':
    bibliography += (r'\label{bib:Smullyan1968}Smullyan, Raymond M. 1968. \emph{First-Order Logic}. New York, NY: Springer.'+'\n'
                     +r'\label{bib:Zuckerman1973}Zuckerman, Martin M. 1973. Formation sequences for propositional formulas. \emph{Notre Dame Journal of Formal Logic} 14(1), 134--138.'+'\n')
src=B/f'{edition}-html.tex'
src.write_text(macros+'\n'.join(texts)+r'\section*{સંપાદકીય નોંધો}'+editorial+bibliography,encoding='utf-8')
cmd=['pandoc',str(src),'-f','latex','-t','html5','--mathml','--standalone','--toc','--number-sections','--shift-heading-level-by=1','--metadata','lang=gu-IN','--metadata',f'title={title}','--css','reader.css?v=3','-o',str(O/f'{edition}.html')]
result=subprocess.run(cmd,capture_output=True,encoding='utf-8',errors='replace')
(B/f'{edition}-pandoc.stderr.txt').write_text(result.stderr,encoding='utf-8')
assert result.returncode==0,result.stderr
soup=BeautifulSoup((O/f'{edition}.html').read_text(encoding='utf-8'),'html.parser')
favicon=soup.new_tag('link',rel='icon',href='data:,')
soup.head.append(favicon)
scope={'functions':'ગણો, સંબંધો અને વિધેયોનાં','size':'ગણો, સંબંધો, વિધેયો અને ગણોના કદનાં','arithmetization':'ગણો, સંબંધો, વિધેયો, ગણોના કદ અને અંકગણિતીકરણનાં','infinite':'ગણો, સંબંધો, વિધેયો, ગણોના કદ, અંકગણિતીકરણ અને અનંત ગણોનાં'}
if edition == 'propositional':
    notice_text = f'આ યંત્ર દ્વારા કરેલો અનુવાદ છે. આ આવૃત્તિમાં ગણો અને વિધેયોના અગાઉના સંપૂર્ણ પ્રકરણો તથા વિધાનાત્મક તર્કશાસ્ત્રના વાક્યરચના અને અર્થવિચારના છ ખંડ છે: ૭૨૨માંથી {coverage_gu} મૂળ એકમો. સંપૂર્ણ ગ્રંથનું કામ ચાલુ છે.'
elif edition == 'proof-systems':
    notice_text = f'આ યંત્ર દ્વારા કરેલો અનુવાદ છે. આ આવૃત્તિમાં અગાઉના સંપૂર્ણ પ્રકરણો તથા નિષ્પત્તિ તંત્રોના પરિચય અને ચાર પદ્ધતિઓના પાંચ સર્વેક્ષણ-ખંડ છે: ૭૨૨માંથી {coverage_gu} મૂળ એકમો. સંપૂર્ણ ગ્રંથનું કામ ચાલુ છે.'
elif edition == 'sequent-calculus':
    notice_text = f'આ યંત્ર દ્વારા કરેલો અનુવાદ છે. આ આવૃત્તિમાં અગાઉના સંપૂર્ણ પ્રકરણો તથા શાસ્ત્રીય પ્રથમ-ક્રમના LK સિક્વન્ટ કલનનું સંપૂર્ણ પ્રકરણ છે: ૭૨૨માંથી {coverage_gu} મૂળ એકમો. સંપૂર્ણ ગ્રંથનું કામ ચાલુ છે.'
elif edition == 'natural-deduction':
    notice_text = f'આ યંત્ર દ્વારા કરેલો અનુવાદ છે. આ આવૃત્તિમાં અગાઉના સંપૂર્ણ પ્રકરણો તથા શાસ્ત્રીય પ્રથમ-ક્રમના સ્વાભાવિક નિગમનનું સંપૂર્ણ પ્રકરણ છે: ૭૨૨માંથી {coverage_gu} મૂળ એકમો. સંપૂર્ણ ગ્રંથનું કામ ચાલુ છે.'
elif edition == 'tableaux':
    notice_text = f'આ યંત્ર દ્વારા કરેલો અનુવાદ છે. આ આવૃત્તિમાં અગાઉના સંપૂર્ણ પ્રકરણો તથા શાસ્ત્રીય પ્રથમ-ક્રમના ચિહ્નિત વિશ્લેષણાત્મક ટેબ્લોનું સંપૂર્ણ પ્રકરણ છે: ૭૨૨માંથી {coverage_gu} મૂળ એકમો. સંપૂર્ણ ગ્રંથનું કામ ચાલુ છે.'
elif edition == 'axiomatic-deduction':
    notice_text = f'આ યંત્ર દ્વારા કરેલો અનુવાદ છે. આ આવૃત્તિમાં અગાઉના સંપૂર્ણ પ્રકરણો તથા શાસ્ત્રીય પ્રથમ-ક્રમની સ્વયંસિદ્ધિમૂલક નિષ્પત્તિનું સંપૂર્ણ પ્રકરણ છે: ૭૨૨માંથી {coverage_gu} મૂળ એકમો. સંપૂર્ણ ગ્રંથનું કામ ચાલુ છે.'
elif edition == 'completeness':
    notice_text = f'આ યંત્ર દ્વારા કરેલો અનુવાદ છે. આ આવૃત્તિમાં અગાઉના સંપૂર્ણ પ્રકરણો તથા શાસ્ત્રીય પ્રથમ-ક્રમના પૂર્ણતા પ્રમેયનું સંપૂર્ણ પ્રકરણ છે: ૭૨૨માંથી {coverage_gu} મૂળ એકમો. સંપૂર્ણ ગ્રંથનું કામ ચાલુ છે.'
elif edition == 'first-order-introduction':
    notice_text = f'આ યંત્ર દ્વારા કરેલો અનુવાદ છે. આ આવૃત્તિમાં અગાઉના સંપૂર્ણ પ્રકરણો તથા પ્રથમ-ક્રમ તર્કશાસ્ત્રનું સંપૂર્ણ પરિચય-પ્રકરણ છે: ૭૨૨માંથી {coverage_gu} મૂળ એકમો. સંપૂર્ણ ગ્રંથનું કામ ચાલુ છે.'
elif edition == 'first-order-syntax':
    notice_text = f'આ યંત્ર દ્વારા કરેલો અનુવાદ છે. આ આવૃત્તિમાં અગાઉના સંપૂર્ણ પ્રકરણો તથા પ્રથમ-ક્રમ તર્કશાસ્ત્રનું સંપૂર્ણ વાક્યરચના-પ્રકરણ છે: ૭૨૨માંથી {coverage_gu} મૂળ એકમો. સંપૂર્ણ ગ્રંથનું કામ ચાલુ છે.'
else:
    notice_text = f'આ યંત્ર દ્વારા કરેલો અનુવાદ છે. આ આવૃત્તિમાં {scope[edition]} સંપૂર્ણ પ્રકરણો છે: ૭૨૨માંથી {coverage_gu} મૂળ એકમો. સંપૂર્ણ ગ્રંથનું કામ ચાલુ છે.'
notice=BeautifulSoup(f'<aside aria-label="આવૃત્તિ વિશે"><p>{notice_text} <a href="../docs/EDITION_NOTES.md">પરિભાષા અને ચકાસણીની વિગતો</a>.</p><p>મૂળ: <a href="https://github.com/OpenLogicProject/OpenLogic">Open Logic Project</a> · <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a> · <a href="https://github.com/KokunoYumeto/OpenLogic-translations">અનુવાદોનું કેન્દ્ર</a>.</p></aside>','html.parser')
soup.header.insert_after(notice.aside)
alts={'union':'બંને ગણોના બધા ઘટકો દર્શાવતો યોગગણ','intersection':'બંને ગણોમાં સામાન્ય ઘટકો દર્શાવતો છેદગણ','difference':'પહેલા ગણમાં હોય અને બીજા ગણમાં ન હોય તેવા ઘટકો'}
alts.update(graph_alt)
alts.update({'function':'ડાબા ગણના દરેક ઘટકથી જમણા ગણમાં એક જ તીર; બે આગતોની કિંમત એક જ હોઈ શકે છે.', 'surjective':'સહપ્રદેશના દરેક ઘટક સુધી ઓછામાં ઓછું એક તીર પહોંચે છે.', 'injective':'જુદા આગતોનાં તીરો જુદી કિંમતો સુધી પહોંચે છે.', 'bijective':'પ્રદેશ અને સહપ્રદેશના ઘટકો વચ્ચે પરસ્પર એક-એક સંગતતા.', 'composition':'ત્રણ ગણો: પહેલાં f વડે ડાબેથી મધ્યમાં, પછી g વડે મધ્યથી જમણે. તૂટક તીરો સીધું પહેલાં f અને પછી gનું સંયોજન દર્શાવે છે.'})
for img in soup.find_all('img'):img['alt']=alts[Path(img['src']).stem]
for box in soup.select('div.center'):
    img=box.find('img')
    if img is None:continue
    figure=soup.new_tag('figure');figure.append(img.extract())
    if (para:=box.find('p')) and para.get_text(strip=True):
        cap=soup.new_tag('figcaption')
        for child in list(para.contents):cap.append(child.extract())
        figure.append(cap)
    box.replace_with(figure)
# Pandoc retains labels in display-math TeX annotations but does not emit DOM
# anchors for them.  Bind aligned axiom labels to their corresponding MathML
# rows; bind isolated display labels to the enclosing formula.
for formula in soup.find_all('math'):
    annotation=formula.find('annotation',attrs={'encoding':'application/x-tex'})
    if annotation is None:continue
    math_labels=re.findall(r'\\label\{([^}]+)\}',annotation.get_text())
    if not math_labels:continue
    rows=formula.find_all('mtr')
    if len(rows)==len(math_labels):
        for row,label in zip(rows,math_labels):row['id']=label
    elif len(math_labels)==1:
        formula['id']=math_labels[0]
    else:
        for label in math_labels:
            anchor=soup.new_tag('span',id=label);anchor['class']='math-label-anchor'
            formula.insert_before(anchor)
ids={e['id'] for e in soup.select('[id]')}
broken=[a['href'] for a in soup.select('a[href^="#"]') if a['href'][1:] not in ids]
assert not broken,broken
expected_images={'functions':11,'size':11,'arithmetization':12,'infinite':13,'propositional':13,'proof-systems':13,'sequent-calculus':13,'natural-deduction':13,'tableaux':13,'axiomatic-deduction':13,'completeness':13,'first-order-introduction':13,'first-order-syntax':13}[edition]
assert len(soup.find_all('img'))==expected_images
assert not soup.select('span.math'), 'Pandoc math conversion fell back to source TeX'
# Source pto is an arrow with an interior vertical stroke, not an ordinary total-function arrow.
partial_count=0
for marker in soup.find_all(['mo','mtext']):
    if marker.get_text()!='GU-PARTIAL-ARROW':continue
    replacement=BeautifulSoup('<mo aria-label="આંશિક વિધેયનું તીર">⇸</mo>','html.parser').mo
    marker.replace_with(replacement);partial_count+=1
assert partial_count==(B/f'{edition}-body.tex').read_text(encoding='utf-8').count(r'\pto'),partial_count
# Preserve the source partial-arrow glyph semantically and visually as a composite MathML operator.
for annotation in soup.select('annotation[encoding="application/x-tex"]'):
    annotation.string=annotation.get_text().replace(r'\mathrel{\text{GU-PARTIAL-ARROW}}',r'\pto')
assert 'GU-PARTIAL-ARROW' not in str(soup)
html = str(soup).replace('\r\n', '\n').replace('\r', '\n')
html = re.sub(r'[ \t]+(?=\n|$)', '', html)
(O/f'{edition}.html').write_text(html,encoding='utf-8',newline='\n')
(B/f'{edition}-html-qa.json').write_text(json.dumps(dict(edition=edition,source_units_covered=coverage,mathml_nodes=len(soup.find_all('math')),images=expected_images,source_labels=len(labels),broken_anchors=broken,graph_incidence=graph_receipts,proof_representations=proof_render_receipts,pandoc_stderr=result.stderr,semantic_review='exact DOM, MathML, link, asset, and character-sequence QA complete; direct local-file browser navigation is recorded separately'),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(edition=edition,source_units_covered=coverage,bytes=(O/f'{edition}.html').stat().st_size,mathml=len(soup.find_all('math')),labels=len(labels),images=expected_images,warnings=result.stderr),ensure_ascii=False))
