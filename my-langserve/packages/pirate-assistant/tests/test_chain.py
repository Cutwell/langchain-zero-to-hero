from pirate_assistant.chain import chain
import langsmith
from datetime import datetime

def test_chain():
	client = langsmith.Client()

	chain_results = client.run_on_dataset(
		dataset_name="pirate-dataset",
		llm_or_chain_factory=chain,
		project_name=f"pirate-dataset-test-{int(datetime.now().strftime('%Y%m%d%H%M%S'))}",
		concurrency_level=5,
		verbose=True,
	)