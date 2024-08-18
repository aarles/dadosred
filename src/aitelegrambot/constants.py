from importlib.metadata import version

WELCOME_MESSAGE: str = f"""
Olá! Bem-vinde! 

Sou um bot baseado em LLM especialista em Data Analytics e Data Science. Você pode me fazer perguntas sobre esses temas e eu procurarei responder da melhor forma possível.

Vamos começar?

PS: bot adaptado de https://github.com/tusharhero/aitelegrambot
"""
HELP_MESSAGE: str = """
*Comandos*:
- /start
- /prompt <query>
- /help
*Comandos administrativos*:
- /list\_models
- /change\_model <model\_name>
- /pull\_model <model\_name>
- /remove\_model <model\_name>
"""

MISTAKEN_CLICK:str = """
You have made a mistake by clicking on the `/infer` \
command directly without providing an input, to do \
this properly please provide a prompt along with the command.
"""
