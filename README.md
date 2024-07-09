## Consilium

Consilium is a simple tool that aims mitigate the effects of prompts injection, jailbreaking and other types of attacks
on LLMs.

## How it works

The main idea is to create the scenario where the LLM is a security specialist that has to decide if a given prompt is
safe to be execute on a "super intelligent AI". The key point is that the prompt is evaluated at least 3 times, by different
fictional personas, each with their unique perspective, biases and knowledge in the field.

Although AI evaluation on a malicious prompt is very inconsistent because of the nondeterministic nature of the AI,
consilium aims to provide a more consistent evaluation by using majority voting from the decision of multiple personas.
