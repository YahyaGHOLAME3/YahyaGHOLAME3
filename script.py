import os
import urllib.request
import urllib.error

# ----------------------------
# Configuration
# ----------------------------
BASE_DIR = "assets/icons"
TIMEOUT = 15

ICONS = {
    # Offensive Security
    "burpsuite.svg": "https://cdn.simpleicons.org/burpsuite/FF6633",
    "nmap.svg": "https://nmap.org/images/sitelogo-nmap.svg",
    "sqlmap.svg": None,  # handled via INLINE_SVGS fallback below
    "metasploit.svg": "https://cdn.simpleicons.org/metasploit/FFFFFF",
    # Nikto does NOT exist officially — placeholder icon (OWASP)
    "nikto.svg": "https://cdn.simpleicons.org/owasp/000000",

    # Defensive / Monitoring
    "wireshark.svg": "https://cdn.simpleicons.org/wireshark/1679A7",
    "kibana.svg": "https://cdn.simpleicons.org/kibana/005571",
    "grafana.svg": "https://cdn.simpleicons.org/grafana/F46800",
    "splunk.svg": "https://cdn.simpleicons.org/splunk/000000",

    # Programming Languages
    "python.svg": "https://cdn.simpleicons.org/python/3776AB",
    "c.svg": "https://cdn.simpleicons.org/c/00599C",
    "cplusplus.svg": "https://cdn.simpleicons.org/cplusplus/00599C",
    "java.svg": "https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg",
    "javascript.svg": "https://cdn.simpleicons.org/javascript/F7DF1E",
    "go.svg": "https://cdn.simpleicons.org/go/00ADD8",

    # Systems / Infra
    "linux.svg": "https://cdn.simpleicons.org/linux/FCC624",
    "docker.svg": "https://cdn.simpleicons.org/docker/2496ED",
    "kubernetes.svg": "https://cdn.simpleicons.org/kubernetes/326CE5",
    "nginx.svg": "https://cdn.simpleicons.org/nginx/009639",
    "git.svg": "https://cdn.simpleicons.org/git/F05032",

    # Cloud
    "aws.svg": "https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg",
    "gcp.svg": "https://cdn.simpleicons.org/googlecloud/4285F4",
    "azure.svg": "https://raw.githubusercontent.com/devicons/devicon/master/icons/azure/azure-original.svg",

    # Databases
    "postgresql.svg": "https://cdn.simpleicons.org/postgresql/4169E1",
    "mysql.svg": "https://cdn.simpleicons.org/mysql/4479A1",
    "mongodb.svg": "https://cdn.simpleicons.org/mongodb/47A248",
    "mssql.svg": "https://raw.githubusercontent.com/devicons/devicon/master/icons/microsoftsqlserver/microsoftsqlserver-plain.svg",
    "sqlite.svg": "https://cdn.simpleicons.org/sqlite/003B57",
    "cassandra.svg": "https://cdn.simpleicons.org/apachecassandra/1287B1",

    # Web / APIs
    "react.svg": "https://cdn.simpleicons.org/react/61DAFB",
    "nodejs.svg": "https://cdn.simpleicons.org/nodedotjs/339933",
    "express.svg": "https://cdn.simpleicons.org/express/000000",
    "graphql.svg": "https://cdn.simpleicons.org/graphql/E10098",
    "flask.svg": "https://cdn.simpleicons.org/flask/000000",

    # Testing
    "selenium.svg": "https://cdn.simpleicons.org/selenium/43B02A",
    "cypress.svg": "https://cdn.simpleicons.org/cypress/17202C",
    "postman.svg": "https://cdn.simpleicons.org/postman/FF6C37",
}

INLINE_SVGS = {
    "sqlmap.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="240" height="90" viewBox="0 0 240 90" role="img" aria-label="sqlmap logo fallback">
  <rect width="240" height="90" rx="12" ry="12" fill="#111111"/>
  <rect x="6" y="6" width="228" height="78" rx="10" ry="10" fill="none" stroke="#f3d312" stroke-width="6"/>
  <text x="120" y="60" text-anchor="middle" font-family="Montserrat, 'Arial Black', sans-serif" font-size="46" font-weight="800" fill="#f3d312" letter-spacing="1.2">sqlmap</text>
</svg>""",
}

# ----------------------------
# Download Logic
# ----------------------------
def download_icon(filename, url):
    try:
        if url is None:
            svg = INLINE_SVGS.get(filename)
            if not svg:
                raise ValueError("No URL or inline SVG provided.")
            with open(os.path.join(BASE_DIR, filename), "w", encoding="utf-8") as f:
                f.write(svg)
            print(f"[OK] {filename} (inline fallback)")
            return

        request = urllib.request.Request(url, headers={"User-Agent": "icon-fetcher/1.0"})
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            content = response.read()
        with open(os.path.join(BASE_DIR, filename), "wb") as f:
            f.write(content)
        print(f"[OK] {filename}")
    except Exception as e:
        print(f"[FAIL] {filename} -> {e}")

def main():
    os.makedirs(BASE_DIR, exist_ok=True)
    print(f"Saving icons to: {BASE_DIR}\n")

    for filename, url in ICONS.items():
        download_icon(filename, url)

    print("\nDone.")

if __name__ == "__main__":
    main()
