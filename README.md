# Engram Memory Plugin for Hermes

The Engram Memory Plugin adds long term memory capabilities to Hermes using Weaviate’s Engram memory platform.

By default, Hermes includes built in memory features designed for short, single session interactions. This plugin extends those capabilities by enabling persistent memory across longer conversations and multiple sessions, making it possible to build agents that can remember and retrieve information over time.

Engram is currently in preview. You can learn more about it here: [Engram Deep Dive](https://weaviate.io/blog/engram-deep-dive?utm_source=chatgpt.com).
If you want to try it out, you can request access here: [Engram Preview Access](https://weaviate.io/product-previews?utm_source=chatgpt.com#preview-engram).

## Installation

Clone the repository:

```bash
git clone https://github.com/Studio1HQ/Hermes_Engram_Plugin
cd Hermes_Engram_Plugin
```

Next, place the plugin inside Hermes’ plugins directory:

```bash
mv engram ~/.hermes/plugins/
```

Hermes automatically discovers plugins from this location.

Enable the plugin:

```bash
hermes plugins enable engram
```

## Verifying the Plugin

To confirm the plugin has been installed correctly, run:

```bash
hermes memory
```

If successful, `engram` should appear as one of the available memory providers.

## Setup

Run the memory setup command:

```bash
hermes memory setup
```

You will be prompted to select a memory provider. Choose `engram` from the list and provide your `ENGRAM_API_KEY` when requested.

Once setup is complete, verify again:

```bash
hermes memory
```

Engram should now be listed as the active memory provider.

## How It Works

Once configured, Hermes will automatically store and retrieve conversation data using Engram after each session. This enables persistent, long term memory beyond the default limits of Hermes’ built in memory system.

