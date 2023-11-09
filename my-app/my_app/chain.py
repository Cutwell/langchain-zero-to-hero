from langchain.chat_models import ChatOpenAI
from langchain import hub


_prompt = hub.pull("cutwell/best-pirate-ever")
_model = ChatOpenAI()

# if you update this, you MUST also update ../pyproject.toml
# with the new `tool.langserve.export_attr`
chain = _prompt | _model
