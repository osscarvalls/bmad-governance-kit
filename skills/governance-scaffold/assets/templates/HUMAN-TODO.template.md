# Human TODO — what only a human can do

> **What this is.** The single index of pending **human-only actions** — so anyone can see them at a glance
> and know what blocks what. Maintained by the agent; read by the human.
>
> **Entry rule (strict).** An item belongs here **only if you can name why a human — not the agent — must do
> it.** Canonical justifications: **payment/billing · a dashboard/OAuth action the agent has no CLI-auth for
> · an exposed/compromised secret · promotion to production · owner sign-off · legal work.** If the agent
> *can* do it, it goes to `AGENT-TODO.md`, not here.
>
> **Item format.** `What · Why-human · Blocks`.
> **States:** 🔴 blocks something active · 🟡 pending, does not block the build · ⚪ deferred (future gate).
>
> **Lifecycle.** Persisted index, not a log. When an item resolves, mark it resolved in-place or remove it
> once nothing references it. Never let a resolved item keep reading as active.

---

## 🔴 Blocking

### 1. <Short title>  ·  (<optional ref/D-NN>)
- **What:** <one-line concrete action>
- **Why-human:** <billing | dashboard/OAuth | exposed secret | prod-promotion | owner sign-off | legal> — <why the agent can't>
- **Blocks:** <what is held up>

---

## 🟡 Pending (does not block continuing to build)

_(none)_

---

## ⚪ Deferred — <named future gate>

_(none)_
