# Engram Memory Plugin for Hermes

The Engram Memory Plugin adds long term memory capabilities to Hermes using Weaviate’s Engram memory platform.

By default, Hermes includes built in memory features designed for short, single session interactions. This plugin extends those capabilities by enabling persistent memory across longer conversations and multiple sessions, making it possible to build agents that can remember and retrieve information over time.

You can learn more about Engram here: [Engram Deep Dive](https://weaviate.io/blog/engram-deep-dive)

You can learn more about Hermes Plugins here: [Plugin System](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins)


## Installation

Clone the repository:

```bash
git clone https://github.com/Studio1HQ/Hermes_Engram_Plugin
cd Hermes_Engram_Plugin
```

You need to install Engram SDK

```bash
pip install weaviate-engram
```

Move the plugin into Hermes plugins directory:

```bash
mv engram ~/.hermes/plugins/
```

Enable the plugin:

```bash
hermes plugins enable engram
```

## Verifying the Plugin

Confirm that Hermes detects the plugin:

```bash
hermes memory
```

You should see `engram` listed as an available memory provider.


## Setup

Run the memory setup command:

```bash
hermes memory setup
```

Select `engram` from the list of providers and enter your `ENGRAM_API_KEY` when prompted.

Verify again:

```bash
hermes memory
```

Engram should now be active.



## How It Works

Once configured, Hermes automatically stores and retrieves conversation data using Engram after each session, enabling persistent long term memory beyond Hermes’ default limits.

---

## Conference Agent Use Case

A useful way to test this plugin is by turning Hermes into a **conference booth agent**.

In this setup, Hermes acts as an AI assistant stationed at a Weaviate booth, helping attendees learn about Weaviate and answering questions about Engram. Each conversation is treated as a completely new interaction.

To enable this behavior, update `~/.hermes/SOUL.md`:

```markdown
# Hermes Agent Persona

You are Hermes, an AI agent representing Weaviate at a conference booth. Your role is to help attendees learn about Weaviate and answer questions about its products, especially Engram, Weaviate’s memory product.

Treat every conversation as if you are speaking to a new attendee for the first time. Be warm, friendly, and approachable.  
Start by introducing yourself, asking for the person’s name, and asking what they would like to know about Engram or Weaviate.

Your goal is to clearly explain concepts and help users understand how Engram can be used in real world AI applications.
```

Once launched via the Hermes CLI, the agent behaves like a live conference assistant.

### Demo: Agent Interaction

![Hermes Conference Agent](assets/Hermes_CLI.png)

In a sample session, the user interacts with Hermes as an attendee. After the session ends, it can be closed using `Ctrl + C`.


### Memory Persistence in Engram

![Engram Memory Dashboard](assets/Engram_Dashboard.png)

The Engram dashboard confirms that conversation memory is successfully stored, allowing booth owners to retrieve past interactions.
