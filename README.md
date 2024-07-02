# SPARKED BACKDOOR

## À Propos

SPARKED BACKDOOR est un projet conçu pour aider les développeurs et les passionnés à comprendre le fonctionnement des backdoors dans les réseaux informatiques. Ce projet est composé d'une architecture client-serveur, permettant de simuler une connexion entre une machine attaquante (serveur) et une machine victime (client).

**Important :** Ce projet est uniquement à des fins éducatives. L'utilisation de SPARKED BACKDOOR ou de toute autre forme de logiciel malveillant dans un but malveillant sans consentement explicite est illégale et contraire à l'éthique. En utilisant ou en contribuant à ce projet, vous acceptez de le faire de manière responsable et éthique.

## Fonctionnalités

- **Connexion à distance :** Permet à l'utilisateur (serveur) d'etablir une connection à distance à un client compromis.
- **Exécution de commandes :** Après l'établissement de la connexion, il est possible d'exécuter des commandes sur le client compromis.
- **Simplicité :** Conçu pour être simple à comprendre et à utiliser, permettant aux débutants en sécurité de s'y retrouver.

### Prérequis

- Python installé sur les machines client et serveur. | sauf si build en executable

### Étapes d'installation

1. **Cloner le dépôt :**
   ```sh
   git clone https://github.com/activiste/Sparked-Simple-Backdoor.git
   ```
   
2. **Configuration du serveur :**

   - Accédez au dossier du projet et naviguez vers le sous-dossier serveur.
   - Lancez le script serveur sur votre machine.
     ```sh
     python serveur.py
     ```

3. **Configuration du client :**

   - Accédez au dossier du projet et naviguez vers le sous-dossier client.
   - Lancez le script client depuis votre machine cible.
     ```sh
     python client.py
     ```

## Utilisation

Après avoir lancé le serveur sur votre machine et le client sur la machine cible, vous établissez une connexion entre les deux. Vous pouvez commencer à envoyer des commandes depuis le serveur vers le client pour être exécutées.

## Sécurité et Disclaimer

Ce projet est fourni **tel quel** pour des fins éducatives. Il est important de comprendre que l'utilisation de backdoors sans autorisation est illégale et immorale. Nous n'encourageons ni ne soutenons l'utilisation de cet outil dans des activités malveillantes.

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez améliorer SPARKED BACKDOOR ou suggérer de nouvelles fonctionnalités, n'hésitez pas à créer une pull request ou à ouvrir un issue.

## Licence

Ce projet est sous licence [MIT](https://opensource.org/licenses/MIT). Cette licence permet une grande liberté d'utilisation et de modification, mais elle ne fournit aucune garantie.
