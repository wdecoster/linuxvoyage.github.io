"""The course structure as shown on the home page.

Section directories under lessons/locales/en_english/ decide what exists and in
what order lessons appear; this decides how sections are grouped into tiers,
what each card says, and which icon it uses. Adding a section means adding a
directory with an order file, and adding an entry here.

Each entry is (title, first lesson slug, icon name, blurb). The icon is the
stem of a file in docs/static/assets/home/ before its hash. There are fewer
icons than sections, so a few are used twice, but never twice within a tier.
"""

TIERS = [
    ("Start here", [
        ("Getting Started", "what-is-linux", "network-configuration",
         "What Linux actually is, then reaching your server with ssh, keys and VS Code."),
        ("Command Line", "the-shell", "command-line",
         "The fundamentals: navigating files and directories, and editing them with nano."),
        ("Text Manipulation", "stdout-standard-out-redirect", "text-fu",
         "Redirection, pipes, and the tools for slicing text: grep, sort, uniq, cut, sed, awk."),
        ("Permissions", "file-permissions", "access",
         "Read, write and execute, and how to change them."),
        ("Scripting", "shell-variables", "text-fu-advanced",
         "Variables, conditionals, loops, running many jobs, and how R and Python fit in."),
        ("Jobs and Processes", "background-jobs", "processes",
         "Background jobs, screen sessions that survive a dropped connection, and htop."),
        ("Moving Data", "downloading-files", "network-sharing",
         "Getting files on and off the server: wget, scp, rsync and tar."),
        ("Your Environment", "env-environment", "package-management",
         "Environment variables, PATH, installing software with conda, and disk space."),
    ]),
    ("Going Further", [
        ("Users and Groups", "users-and-groups", "user-management",
         "Accounts, groups, root and sudo, and the files behind them."),
        ("Packages", "software-distribution", "package-management",
         "Package managers, repositories, and building from source."),
        ("Advanced ssh", "ssh-config-and-agents", "subnetting",
         "Config files, agents, jump hosts and port forwarding, once the basics chafe."),
        ("Process Utilization", "tracking-processes-top", "process-utilization",
         "Monitoring CPU, memory and I/O, and scheduling work with cron."),
        ("Logging", "system-logging", "logging",
         "Where the system writes things down, and how to read it."),
    ]),
    ("Under the Hood", [
        ("Linux Distributions", "linux-history", "getting-started",
         "Where Linux came from, and how Ubuntu, Debian, Red Hat and the rest differ."),
        ("The Filesystem", "filesystem-hierarchy", "filesystem",
         "Disks, partitions, mounting, inodes and symlinks."),
        ("Devices", "dev-directory", "devices",
         "How Linux represents the hardware attached to your machine."),
        ("Boot the System", "boot-process-overview", "booting",
         "What happens between power on and a login prompt."),
        ("Kernel", "kernel-overview", "kernel",
         "The core of the operating system, modules and system calls."),
        ("Init", "sysv-overview", "init",
         "How services get started, from SysV through to systemd."),
    ]),
    ("Networking", [
        ("Network Fundamentals", "network-basics", "network-fundamentals",
         "The models and layers that networking is built on."),
        ("Subnetting", "ipv4", "subnetting",
         "IPv4, subnet math, CIDR, NAT and IPv6."),
        ("Routing", "what-is-a-router", "routing",
         "Routers, routing tables and the protocols between them."),
        ("Network Configuration", "network-interfaces", "network-configuration",
         "Interfaces, routes, DHCP and ARP."),
        ("Network Troubleshooting", "icmp", "network-troubleshooting",
         "ping, traceroute, netstat and packet analysis."),
        ("DNS", "what-is-dns", "dns",
         "Everything and more that you wanted to know about DNS."),
    ]),
]
