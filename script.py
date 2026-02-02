import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent / "assets" / "icons"
TIMEOUT = 15

# Each icon maps to one or more candidate URLs (SVG or PNG). First successful download wins.
ICONS = {
    # Offensive Security
    "burpsuite.svg": ["https://cdn.simpleicons.org/burpsuite/FF6633"],
    "nmap.svg": ["https://nmap.org/images/sitelogo-nmap.svg"],
    "nikto.svg": ["https://cdn.simpleicons.org/owasp/000000"],
    "sqlmap.png": ["https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/doc/images/sqlmap-logo.png",
                   "https://opengraph.githubassets.com/1/sqlmapproject/sqlmap"],
    "metasploit.svg": ["https://cdn.simpleicons.org/metasploit/FFFFFF"],
    "wireshark.svg": ["https://cdn.simpleicons.org/wireshark/1679A7"],

    # Identity & Active Directory
    "bloodhound.png": ["https://raw.githubusercontent.com/SpecterOps/BloodHound-Legacy/master/docs/images/bloodhound-logo.png"],
    "sharphound.png": ["https://opengraph.githubassets.com/1/SpecterOps/SharpHound"],
    "rubeus.png": ["https://opengraph.githubassets.com/1/GhostPack/Rubeus"],
    "powerview.png": ["https://opengraph.githubassets.com/1/PowerShellMafia/PowerSploit"],

    # Programming Languages
    "python.svg": ["https://cdn.simpleicons.org/python/3776AB"],
    "c.svg": ["https://cdn.simpleicons.org/c/00599C"],
    "cplusplus.svg": ["https://cdn.simpleicons.org/cplusplus/00599C"],
    "java.svg": ["https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg"],
    "javascript.svg": ["https://cdn.simpleicons.org/javascript/F7DF1E"],
    "go.svg": ["https://cdn.simpleicons.org/go/00ADD8"],

    # Scripting & Automation
    "bash.svg": ["https://cdn.simpleicons.org/gnubash/4EAA25"],
    "powershell.svg": ["https://raw.githubusercontent.com/devicons/devicon/master/icons/powershell/powershell-original.svg"],
    "cron.svg": ["https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/clock-rotate-left.svg"],

    # Operating Systems
    "kalilinux.svg": ["https://cdn.simpleicons.org/kalilinux/557C94"],
    "ubuntu.svg": ["https://cdn.simpleicons.org/ubuntu/E95420"],
    "debian.svg": ["https://cdn.simpleicons.org/debian/A81D33"],
    "windows.svg": ["https://raw.githubusercontent.com/devicons/devicon/master/icons/windows8/windows8-original.svg"],
    "windowsserver.svg": ["https://raw.githubusercontent.com/devicons/devicon/master/icons/windows8/windows8-original.svg"],

    # Web & App Stack
    "react.svg": ["https://cdn.simpleicons.org/react/61DAFB"],
    "nodejs.svg": ["https://cdn.simpleicons.org/nodedotjs/339933"],
    "express.svg": ["https://cdn.simpleicons.org/express/000000"],
    "postman.svg": ["https://cdn.simpleicons.org/postman/FF6C37"],
    "selenium.svg": ["https://cdn.simpleicons.org/selenium/43B02A"],
    "cypress.svg": ["https://cdn.simpleicons.org/cypress/17202C"],

    # Cloud & Infrastructure
    "aws.svg": ["https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg"],
    "gcp.svg": ["https://cdn.simpleicons.org/googlecloud/4285F4"],
    "azure.svg": ["https://raw.githubusercontent.com/devicons/devicon/master/icons/azure/azure-original.svg"],
    "docker.svg": ["https://cdn.simpleicons.org/docker/2496ED"],
    "kubernetes.svg": ["https://cdn.simpleicons.org/kubernetes/326CE5"],
    "linux.svg": ["https://cdn.simpleicons.org/linux/FCC624"],
    "nginx.svg": ["https://cdn.simpleicons.org/nginx/009639"],

    # Cloud Security
    "iam.png": ["https://www.awsicon.com/static/images/Service-Icons/Security-Identity-Compliance/64/png/Identity-and-Access-Management.png"],
    "terraform.svg": ["https://cdn.simpleicons.org/terraform/7B42BC"],
    "awsorganizations.png": ["https://www.awsicon.com/static/images/Service-Icons/Management-Governance/64/png/Organizations.png"],

    # Networking (using recognizable tech/protocol symbols)
    "tcpip.png": ["https://raw.githubusercontent.com/google/material-design-icons/master/png/social/public/materialicons/48dp/2x/baseline_public_black_48dp.png"],
    "dns.png": ["https://raw.githubusercontent.com/google/material-design-icons/master/png/action/dns/materialicons/48dp/2x/baseline_dns_black_48dp.png"],
    "http.png": ["https://raw.githubusercontent.com/google/material-design-icons/master/png/action/http/materialicons/48dp/2x/baseline_http_black_48dp.png"],
    "smb.png": ["https://upload.wikimedia.org/wikipedia/commons/8/8d/Samba_logo.svg",
                "https://opengraph.githubassets.com/1/samba-team/samba",
                "https://raw.githubusercontent.com/google/material-design-icons/master/png/device/hub/materialicons/48dp/2x/baseline_hub_black_48dp.png"],
    "ldap.png": ["https://upload.wikimedia.org/wikipedia/commons/0/0e/OpenLDAP_logo.svg",
                 "https://raw.githubusercontent.com/google/material-design-icons/master/png/social/group/materialicons/48dp/2x/baseline_group_black_48dp.png"],
    "kerberos.png": ["https://upload.wikimedia.org/wikipedia/commons/3/3a/Kerberos-logo.png",
                     "https://raw.githubusercontent.com/google/material-design-icons/master/png/communication/vpn_key/materialicons/48dp/2x/baseline_vpn_key_black_48dp.png"],

    # CI/CD & Supply Chain
    "githubactions.svg": ["https://cdn.simpleicons.org/githubactions/2088FF"],
    "gitlabci.svg": ["https://cdn.simpleicons.org/gitlab/FC6D26"],
    "jenkins.svg": ["https://cdn.simpleicons.org/jenkins/D24939"],

    # Observability & DevOps
    "grafana.svg": ["https://cdn.simpleicons.org/grafana/F46800"],
    "kibana.svg": ["https://cdn.simpleicons.org/kibana/005571"],
    "git.svg": ["https://cdn.simpleicons.org/git/F05032"],
    "github.svg": ["https://cdn.simpleicons.org/github/181717"],
    "elk.svg": ["https://cdn.simpleicons.org/elasticstack/005571"],

    # Detection / Defensive
    "yara.png": ["https://raw.githubusercontent.com/VirusTotal/yara/master/extra/old-logo.png"],

    # Databases
    "postgresql.svg": ["https://cdn.simpleicons.org/postgresql/4169E1"],
    "mysql.svg": ["https://cdn.simpleicons.org/mysql/4479A1"],
    "mongodb.svg": ["https://cdn.simpleicons.org/mongodb/47A248"],
    "mssql.svg": ["https://raw.githubusercontent.com/devicons/devicon/master/icons/microsoftsqlserver/microsoftsqlserver-plain.svg"],
    "sqlite.svg": ["https://cdn.simpleicons.org/sqlite/003B57"],
    "cassandra.svg": ["https://cdn.simpleicons.org/apachecassandra/1287B1"],
}


def download_first(urls: list[str], dest: Path) -> bool:
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "icon-fetcher/1.1"})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                content = resp.read()
            dest.parent.mkdir(parents=True, exist_ok=True)
            with open(dest, "wb") as f:
                f.write(content)
            print(f"[OK] {dest.name} <- {url}")
            return True
        except Exception as e:
            print(f"[RETRY] {dest.name} failed {url} -> {e}")
    print(f"[FAIL] {dest.name} (all sources)")
    return False


def main() -> None:
    print(f"Saving icons to: {BASE_DIR}\n")
    for filename, sources in ICONS.items():
        if isinstance(sources, str):
            sources = [sources]
        download_first(sources, BASE_DIR / filename)
    print("\nDone.")


if __name__ == "__main__":
    main()
