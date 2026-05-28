# Engram Memory Plugin for Hermes

The Engram Memory Plugin adds long term memory capabilities to Hermes using Weaviate’s Engram memory platform.

By default, Hermes includes built in memory features. The Engram plugin extends those capabilities, allowing your agent to retain and retrieve information beyond the default memory limits. This makes it possible to build agents with persistent memory across longer conversations and sessions.

## Installation

Clone the repository:

```bash
git clone <repo-url>
```

Move the plugin into the Hermes plugins directory:

```bash
mv engram ~/.hermes/plugins/
```

Enable the plugin:

```bash
hermes plugins enable engram
```

## Verifying the Plugin

To confirm the plugin is available, run:

```bash
hermes memory
```

You should see `engram` listed as one of the available memory providers.

## Setup

Run the setup command:

```bash
hermes memory setup
```

Select `engram` from the list of memory providers and provide your `ENGRAM_API_KEY` when prompted.

## How It Works

Once configured, Hermes will automatically commit conversation data to Engram after each interaction. This allows your agent to build persistent memory over time and retrieve relevant context across conversations.

