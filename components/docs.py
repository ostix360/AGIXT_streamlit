import streamlit as st


def agixt_docs():
    st.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-Sponsor%20Josh%20XT-blue?logo=github&style=plastic)](https://github.com/sponsors/Josh-XT) [![PayPal](https://img.shields.io/badge/PayPal-Sponsor%20Josh%20XT-blue.svg?logo=paypal&style=plastic)](https://paypal.me/joshxt) [![Ko-Fi](https://img.shields.io/badge/Kofi-Sponsor%20Josh%20XT-blue.svg?logo=kofi&style=plastic)](https://ko-fi.com/joshxt)"
    )

    st.markdown(
        "[![Documentation](https://img.shields.io/badge/Documentation-AGiXT-blue?logo=github&style=plastic)](https://josh-xt.github.io/AGiXT/) [![GitHub](https://img.shields.io/badge/GitHub-AGiXT-blue?logo=github&style=plastic)](https://github.com/Josh-XT/AGiXT) [![Discord](https://img.shields.io/discord/1097720481970397356?label=Discord&logo=discord&logoColor=white&style=plastic&color=5865f2)](https://discord.gg/d3TkHRZcjD) [![Twitter](https://img.shields.io/badge/Twitter-Follow_@Josh__XT-blue?logo=twitter&style=plastic)](https://twitter.com/Josh_XT)"
    )


def predefined_injection_variables():
    st.markdown(
        """
### Predefined Injection Variables
- `{agent_name}` will cause the agent name to be injected.
- `{context}` will cause the current context from memory to be injected. This will only work if you have `{user_input}` in your prompt arguments for the memory search.
- `{date}` will cause the current date and timestamp to be injected.
- `{conversation_history}` will cause the conversation history to be injected.
- `{COMMANDS}` will cause the available commands list to be injected and for automatic commands execution from the agent based on its suggestions.
- `{command_list}` will cause the available commands list to be injected, but will not execute any commands the AI chooses. Useful on validation steps.
- `{STEPx}` will cause the step `x` response from a chain to be injected. For example, `{STEP1}` will inject the first step's response in a chain.
    """
    )
