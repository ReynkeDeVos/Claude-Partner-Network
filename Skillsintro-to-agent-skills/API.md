# API

## Implementing a chat

Angenommen jedes Wort eines Satztes ist ein Token.

Jedes Wort kann viele Bedeutungen haben.
Diese stehen in den "Embeddings" jedes Worts.

Danach findet "contextualization" statt. Das Wort wir angeschaut nach den vorangegangenen und nachfolgenden Wörtern.

Wenn ein Antwortsatz generiert wird, wird nicht nur das wahrscheinlichste Wort ausgegeben, sondern auch ein paar Zufällige.

Am Ende der Antwort wird geschaut, ob alle Konditionen erfüllt sind für die Antwort.

## Temperature

Claude might assign a 30% probability to "about", 20% to "would", 10% to "of", and so on. The model then selects one token and repeats this entire process to build complete sentences.

At low temperatures (near 0), Claude becomes very deterministic - it almost always picks the highest probability token. At high temperatures (near 1), Claude distributes probability more evenly across options, leading to more varied and creative outputs.

### Low Temperature (0.0 - 0.3)

- Factual responses
- Coding assistance
- Data extraction
- Content moderation

### Medium Temperature (0.4 - 0.7)

- Summarization
- Educational content
- Problem-solving
- Creative writing with constraints

### High Temperature (0.8 - 1.0)

- Brainstorming
- Creative writing
- Marketing content
- Joke generation
