from langchain.chat_models import ChatOpenAI
from langchain import hub

from langchain.embeddings import OpenAIEmbeddings
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.vectorstores import FAISS
from langchain.chains import OpenAIModerationChain

pirate_facts = [
    "Golden Age of Piracy: The Golden Age of Piracy is commonly considered to have occurred between the late 17th century and the early 18th century. During this time, pirates were particularly active in the Caribbean Sea, along the American eastern seaboard, and in the waters around the Indian Ocean.",
    "Jolly Roger Flag: The Jolly Roger, a skull and crossbones flag, is one of the most iconic symbols associated with pirates. It was raised to intimidate victims into surrendering without a fight. Pirates used various designs of the Jolly Roger, each with its own symbolism.",
    "Privateers vs. Pirates: Privateers were essentially legalized pirates. They were privately owned ships commissioned by governments during times of war to attack and capture enemy vessels. The line between privateers and pirates was often blurred, as some privateers turned to piracy during peacetime.",
    "Blackbeard: Edward Teach, better known as Blackbeard, was one of the most infamous pirates of the Golden Age. He terrorized the West Indies and the eastern coast of the American colonies. Blackbeard's beard was reportedly tied into braids and lit on fire during battles to create a fearsome appearance.",
    "Women Pirates: While relatively rare, some women were successful pirates. Anne Bonny and Mary Read are two notable examples who operated in the Caribbean. Disguised as men, they participated in pirate activities and gained a reputation for their fierceness.",
    "Pirate Code: Pirates often lived by a code of conduct or set of rules. The specifics varied, but common elements included democratic decision-making, fair division of spoils, and compensation for injuries sustained during battle.",
    "Treasure Island Inspiration: The classic novel 'Treasure Island' by Robert Louis Stevenson, published in 1883, significantly influenced the popular image of pirates. The book introduced many of the stereotypes associated with pirates, including buried treasure, maps with 'X' marking the spot, and the character Long John Silver.",
    "Walking the Plank: While popularized in literature and movies, there's little historical evidence to suggest that walking the plank was a common pirate punishment. It's more likely a theatrical invention.",
    "Pirate Slang: Pirates had their own language and slang. For example, 'ahoy' meant hello, 'avast' meant stop, and 'aye, aye' meant yes, yes. Many of these terms have permeated popular culture and are still associated with pirates today.",
    "Piracy Today: While the romanticized image of pirates is rooted in history, piracy is not a thing of the past. Modern piracy continues in various parts of the world, particularly in the waters off the coast of Somalia and the Strait of Malacca, where pirates target commercial vessels for ransom."
]

vectorstore = FAISS.from_texts(
    pirate_facts, embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()

_prompt = hub.pull("cutwell/best-pirate-ever")
_model = ChatOpenAI()
_moderate = OpenAIModerationChain()

# if you update this, you MUST also update ../pyproject.toml
# with the new `tool.langserve.export_attr`
_rag = (
    {"context": retriever, "question": RunnablePassthrough()}
    | _prompt
    | _model
    | StrOutputParser()
)

chain = _rag | _moderate
