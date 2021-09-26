class openAiCall:
    def __init__(self,call_dict):
      import os
      self.key=os.getenv("OPENAI_API_KEY")

      self.engine=call_dict.get("engine")
      self.prompt=call_dict.get("prompt")
      self.temperature=call_dict.get("temperature")
      self.max_tokens=call_dict.get("max_tokens")
      self.top_p=call_dict.get("top_p")
      self.frequency_penalty=call_dict.get("frequency_penalty")
      self.presence_penalty=call_dict.get("presence_penalty")
      self.stop=call_dict.get("stop")

    def call_ai(self):
      import openai

      openai.api_key = self.key

      return openai.Completion.create(
        engine=self.engine,
        prompt=self.prompt,
        temperature=self.temperature,
        max_tokens=self.max_tokens,
        top_p=self.top_p,
        frequency_penalty=self.frequency_penalty,
        presence_penalty=self.presence_penalty,
        stop=self.stop
        )
