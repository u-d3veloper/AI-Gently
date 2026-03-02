## Architecture cible

### Définitions
- `langchain` est framework python pour orchestrer les actions et le rôle de notre agent (sa mémoire, les tools, RAG, etc.)
- Mistral et son api pour les modèles LLM (choix personel, doit pouvoir être adaptable à d'autres providers)
- Les tools sont les fonctions python qui appellent des APIs (météo, notion, github, etc) et que l'agent peut invoquer
- MCP : un protocole standardisé pour exposer ces outils sous forme de serveurs consommables par divers hosts (IDE, chatbots etc) sera éventuellement utilisable plus tard

### Objectif de la v0 : 
- Un agent basique langchain qui tourne en local, (CLI ou serveur fastapi)
- Un modèle mistral via l'API
- Des tools simples (appels à des API ou des MCP)

