import { readFileSync, writeFileSync } from "node:fs";

const path = new URL("./book/include/glossary.tex", import.meta.url);
const source = readFileSync(path, "utf8");
const entry = /^\\slcterm(?:\[[^\n]*\])?\{([^}]+)\}\{(\d{3})\}\{([^}]+)\}/gm;
const records = Array.from(source.matchAll(entry));
const collator = new Intl.Collator("gu");
const sortTitle = (title) => title.replace(/^\$x\$-/, "").replaceAll("--", " ");
records.sort((a, b) => collator.compare(sortTitle(a[3]), sortTitle(b[3])) ||
  a[1].localeCompare(b[1], "en"));
const keys = new Map(records.map((record, index) => [record[1], String(index + 1).padStart(3, "0")]));
const sorted = source.replace(entry, (match, id, oldKey) =>
  match.replace("{" + id + "}{" + oldKey + "}", "{" + id + "}{" + keys.get(id) + "}"));
if (process.argv.includes("--check")) {
  if (source !== sorted) throw new Error("Gujarati glossary sort keys are out of date");
} else {
  writeFileSync(path, sorted);
}
