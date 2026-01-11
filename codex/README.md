# Codex Packet Contracts

This directory contains one **authoritative contract file per packet** in the locked queue.

Usage pattern:
1. Copy the packet file into a GitHub issue body (or commit it into the issue branch at `control/packets/issue-XX-<packet_id>.md`).
2. Create the issue-linked branch/PR yourself.
3. Put `Closes #XX` in the PR description.
4. Hand Codex a short prompt pointing to the in-repo contract file path.

Packets:
- Packet 2: deterministic cache/replay
- Packet 3: OPA memoization
- Packet 4: external GEN executor hook
- Packet 5: mechanical CHECK enforcement
- Packet 6: PROMOTE implementation
