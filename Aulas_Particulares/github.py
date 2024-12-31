from github import Github

# Authentication is defined via github.Auth
from github import Auth

# using an access token
auth = Auth.Token("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")

# Public Web Github
g = Github(auth=auth)

# Github Enterprise with custom hostname
g = Github(auth=auth, base_url="https://github.com/leonidasprof/api/v3")

# Exemplo de uso: obter informações do usuário autenticado
user = g.get_user()
print(user.login)
