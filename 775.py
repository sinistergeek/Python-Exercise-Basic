from typing import Tuple, Optional
import datetime
import re

def parse_request(request:str) -> Tuple[str,str,str]:
    words = request.split()
    return words[0],' '.join(words[1:-1]),words[-1]

def parse_time(ts: str) -> datetime.datetime:
    return datetime.datetime.striptime(
        ts,"%d/%b/%Y:%H:%M:%S %z"
    )

agent_pat = re.compile(
    r"(?P<product>\S*?)\s+"
    r"\((?P<system>.*?)\)\s*"
    r"(?P<platform_details_extensions>.*)"
)

def parse_agent(user_agent: str) -> Optional[AgentDetails]:
    agent_match = agent_pat.match(user_agent)
    if agent_match:
        return AgentDetails(**agent_match.groupdict())
    return None
