import urllib.request
from pathlib import Path

# ----------------------------
# Configuration
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent / "assets" / "icons"
TIMEOUT = 15


def make_badge(label: str, bg: str = "#111111", fg: str = "#f3d312") -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="200" height="80" viewBox="0 0 200 80" role="img" aria-label="{label}">
<rect width="200" height="80" rx="12" ry="12" fill="{bg}"/>
<rect x="6" y="6" width="188" height="68" rx="10" ry="10" fill="none" stroke="{fg}" stroke-width="4"/>
<text x="100" y="50" text-anchor="middle" font-family="Montserrat,'Arial Black',sans-serif" font-size="24" font-weight="800" fill="{fg}">{label}</text>
</svg>"""


ICONS = {
    # Offensive Security
    "burpsuite.svg": "https://cdn.simpleicons.org/burpsuite/FF6633",
    "nmap.svg": "https://nmap.org/images/sitelogo-nmap.svg",
    "nikto.svg": "https://cdn.simpleicons.org/owasp/000000",
    "sqlmap.svg": None,  # inline fallback
    "metasploit.svg": "https://cdn.simpleicons.org/metasploit/FFFFFF",
    "wireshark.svg": "https://cdn.simpleicons.org/wireshark/1679A7",

    # Identity & Active Directory
    "bloodhound.svg": None,
    "sharphound.svg": None,
    "rubeus.svg": None,
    "powerview.svg": None,

    # Programming Languages / Scripting
    "python.svg": "https://cdn.simpleicons.org/python/3776AB",
    "c.svg": "https://cdn.simpleicons.org/c/00599C",
    "cplusplus.svg": "https://cdn.simpleicons.org/cplusplus/00599C",
    "java.svg": "https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg",
    "javascript.svg": "https://cdn.simpleicons.org/javascript/F7DF1E",
    "bash.svg": "https://cdn.simpleicons.org/gnubash/4EAA25",
    "powershell.svg": "https://raw.githubusercontent.com/devicons/devicon/master/icons/powershell/powershell-original.svg",
    "go.svg": "https://cdn.simpleicons.org/go/00ADD8",
    "cron.svg": None,

    # Operating Systems
    "kalilinux.svg": "https://cdn.simpleicons.org/kalilinux/557C94",
    "ubuntu.svg": "https://cdn.simpleicons.org/ubuntu/E95420",
    "debian.svg": "https://cdn.simpleicons.org/debian/A81D33",
    "windows.svg": "https://raw.githubusercontent.com/devicons/devicon/master/icons/windows8/windows8-original.svg",
    "windowsserver.svg": "https://raw.githubusercontent.com/devicons/devicon/master/icons/windows8/windows8-original.svg",

    # Web & App Stack
    "react.svg": "https://cdn.simpleicons.org/react/61DAFB",
    "nodejs.svg": "https://cdn.simpleicons.org/nodedotjs/339933",
    "express.svg": "https://cdn.simpleicons.org/express/000000",
    "postman.svg": "https://cdn.simpleicons.org/postman/FF6C37",
    "selenium.svg": "https://cdn.simpleicons.org/selenium/43B02A",
    "cypress.svg": "https://cdn.simpleicons.org/cypress/17202C",

    # Cloud & Infrastructure
    "aws.svg": "https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg",
    "gcp.svg": "https://cdn.simpleicons.org/googlecloud/4285F4",
    "azure.svg": "https://raw.githubusercontent.com/devicons/devicon/master/icons/azure/azure-original.svg",
    "docker.svg": "https://cdn.simpleicons.org/docker/2496ED",
    "kubernetes.svg": "https://cdn.simpleicons.org/kubernetes/326CE5",
    "linux.svg": "https://cdn.simpleicons.org/linux/FCC624",
    "nginx.svg": "https://cdn.simpleicons.org/nginx/009639",

    # Cloud Security
    "iam.svg": None,
    "terraform.svg": "https://cdn.simpleicons.org/terraform/7B42BC",
    "awsorganizations.svg": None,

    # Networking
    "tcpip.svg": None,
    "dns.svg": None,
    "http.svg": None,
    "smb.svg": None,
    "ldap.svg": None,
    "kerberos.svg": None,

    # CI/CD & Supply Chain
    "githubactions.svg": "https://cdn.simpleicons.org/githubactions/2088FF",
    "gitlabci.svg": "https://cdn.simpleicons.org/gitlab/FC6D26",
    "jenkins.svg": "https://cdn.simpleicons.org/jenkins/D24939",

    # Observability & DevOps
    "grafana.svg": "https://cdn.simpleicons.org/grafana/F46800",
    "kibana.svg": "https://cdn.simpleicons.org/kibana/005571",
    "git.svg": "https://cdn.simpleicons.org/git/F05032",
    "github.svg": "https://cdn.simpleicons.org/github/181717",
    "elk.svg": "https://cdn.simpleicons.org/elasticstack/005571",

    # Detection / Defensive
    "yara.svg": None,

    # Databases
    "postgresql.svg": "https://cdn.simpleicons.org/postgresql/4169E1",
    "mysql.svg": "https://cdn.simpleicons.org/mysql/4479A1",
    "mongodb.svg": "https://cdn.simpleicons.org/mongodb/47A248",
    "mssql.svg": "https://raw.githubusercontent.com/devicons/devicon/master/icons/microsoftsqlserver/microsoftsqlserver-plain.svg",
    "sqlite.svg": "https://cdn.simpleicons.org/sqlite/003B57",
    "cassandra.svg": "https://cdn.simpleicons.org/apachecassandra/1287B1",
}

INLINE_SVGS = {
    "sqlmap.svg": make_badge("sqlmap"),
    "bloodhound.svg": make_badge("BloodHound"),
    "sharphound.svg": make_badge("SharpHound"),
    "rubeus.svg": make_badge("Rubeus"),
    "powerview.svg": make_badge("PowerView"),
    "cron.svg": make_badge("Cron"),
    "iam.svg": make_badge("IAM"),
    "awsorganizations.svg": make_badge("AWS Orgs"),
    "tcpip.svg": make_badge("TCP/IP"),
    "dns.svg": make_badge("DNS"),
    "http.svg": make_badge("HTTP/S"),
    "smb.svg": make_badge("SMB"),
    "ldap.svg": make_badge("LDAP"),
    "kerberos.svg": make_badge("Kerberos"),
    "yara.svg": make_badge("YARA"),
}


def download_icon(filename: str, url: str | None) -> None:
    try:
        if url is None:
            svg = INLINE_SVGS.get(filename)
            if not svg:
                raise ValueError("No URL or inline SVG provided.")
            (BASE_DIR).mkdir(parents=True, exist_ok=True)
            with open(BASE_DIR / filename, "w", encoding="utf-8") as f:
                f.write(svg)
            print(f"[OK] {filename} (inline fallback)")
            return

        req = urllib.request.Request(url, headers={"User-Agent": "icon-fetcher/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
            content = response.read()
        BASE_DIR.mkdir(parents=True, exist_ok=True)
        with open(BASE_DIR / filename, "wb") as f:
            f.write(content)
        print(f"[OK] {filename}")
    except Exception as e:
        print(f"[FAIL] {filename} -> {e}")


def main() -> None:
    print(f"Saving icons to: {BASE_DIR}\n")
    for filename, url in ICONS.items():
        download_icon(filename, url)
    print("\nDone.")


if __name__ == "__main__":
    main()
