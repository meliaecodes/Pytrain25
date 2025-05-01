https://developer.atlassian.com/platform/atlas-tunnel-cli/usage/getting-started/

brew services start cloudflared

atlas tunnel start --public --port 8080

This will create a private (default) tunnel [StaffID].private.atlastunnel.com → local port 8080

