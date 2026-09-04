from dataclasses import dataclass
import re

PATTERNS={"aws_access_key":re.compile(r"AKIA[0-9A-Z]{16}"),"generic_token":re.compile(r"(?i)(?:token|secret|password|api[_-]?key)\s*[:=]\s*[\"']([^\"']{8,})")}
@dataclass(frozen=True)
class Finding:
    rule:str
    line:int
    value:str

def scan(text:str)->list[Finding]:
    out=[]
    for line_no,line in enumerate(text.splitlines(),1):
        for rule,pattern in PATTERNS.items():
            for match in pattern.finditer(line):
                value=match.group(0)
                out.append(Finding(rule,line_no,value[:8]+"..."))
    return out
