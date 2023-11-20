# Examples → Prompts
 Examples of various useful prompt engineering techniques.

Examples found in the [Prompt Engineering Guide](https://www.promptingguide.ai/techniques). Check out this free online guide for more in-depth discussion of these techniques (and others).

|Prompt Technique|File|Description|
|:---:|:---:|:---:|
|Roleplay|`character_roleplay.md`|Using roleplay to prompt the LLM to behave like a certain character.|
|Zero-shot prompting|`zero_shot.md`|Describing intended output in natural language, without giving examples of this behaviour.|
|Few-shot prompting|`few_shot.md`|Providing examples of desired LLM behaviour (to demonstrate unintuitive mappings between input and output). Useful for both conversational and code-based outputs.|
|Automatic Chain-of-thought|`auto_cot.md`|Induce chain-of-thought reasoning to LLM responses via the key phrase "Let's think step by step" [[Zhang et al. (2022)]](https://arxiv.org/abs/2210.03493)|
|Retrieval Augmented Generation|`rag.md`|Extending the LLMs knowledge by introducing additional context (i.e.: articles / API information (e.g.: weather) / etc.) that can focus the model response. This is most valuable in introducing information previously unknown to the LLM and enabling it to reason over it (i.e.: articles written after the LLM was trained / internal company information (❗ Note: only share this information inside enterprise sandboxes, not to public LLMs like ChatGPT!) / etc.|