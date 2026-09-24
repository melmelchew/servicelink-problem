# The ServiceLink Problem

A point-and-click adventure game about **product thinking** — diagnosing the right problem before building a solution.

**▶ [Play it](https://melmelchew.github.io/servicelink-problem/)**

---

## The premise

Six months ago ServiceLink launched. On time. Under budget. A defect rate low enough to be framed on a wall.

Nobody uses it. This morning it became your problem.

Search the rooms, talk to people, gather evidence — then make eight decisions you cannot take back.

## How it works

Eight scenes, eight decisions, thirteen pieces of evidence.

Each decision sits in a location you have to search first. Click the glowing hotspots to look at things and talk to people: the counter officer who has been saying the same thing for nine years, the man in the queue who isn't angry but has budgeted a third morning, the colleague from Health who validated a service with a spreadsheet.

**You cannot make a decision until you hold the evidence that location requires.** Reach for the action too early and the game tells you why you're not ready.

Exactly one of the thirteen evidence items is optional — the abandonment logs on your own desk. You can answer the problem-statement decision correctly without them and still score the point, but the story forks, and one badge is withheld. Knowing the framework and having done the work are not the same thing.

## The material

Every decision is drawn from Singapore's **[Institute of Digital Government](https://www.idg.gov.sg/product-thinking/)** Product Thinking pathway (AI Build 301), and each explanation links back to the guide it came from:

| Decision | Module |
|---|---|
| Why a well-executed project still failed | [Understanding the Problem](https://www.idg.gov.sg/guides-and-resources/productthinking1/) |
| Which cause in the chain to target | [Start With The Whys](https://www.idg.gov.sg/guides-and-resources/productthinking2/) |
| What the problem statement is missing | [Craft a Clear Problem Statement](https://www.idg.gov.sg/guides-and-resources/productthinking3/) |
| Defining what "it worked" means | [Key Takeaways](https://www.idg.gov.sg/guides-and-resources/productthinking7/) |
| Leading and lagging indicators | [Metrics](https://www.idg.gov.sg/guides-and-resources/productthinking4/) |
| How much weight a Value-Cost Ratio carries | [Metrics](https://www.idg.gov.sg/guides-and-resources/productthinking4/) |
| Eleven weeks of engineering, or something cheaper | [Assumptions and Risks](https://www.idg.gov.sg/guides-and-resources/productthinking5/) |
| What one letter in eleven weeks means | [A Good Customer Experience](https://www.idg.gov.sg/guides-and-resources/productthinking6/) |

## Technical notes

- **One file.** `index.html` — no frameworks, no build step, no backend, no network requests. Open it from disk and it works offline.
- **Scene art is inline SVG**, composed from a handful of primitives and coloured through CSS custom properties, so light and dark themes both work.
- **Options are shuffled every run** (Fisher-Yates). The data authors the correct answer first for legibility; position never indicates the answer.
- **`localStorage` holds only a personal best**, wrapped so a private window degrades to "no best score" rather than breaking.
- **Accessibility:** real buttons, `aria-live` narration, keyboard play (`1`–`4` to decide, `Enter` to continue), and `prefers-reduced-motion` respected.

`quiz-standalone.html` is an earlier, simpler version: the same eight questions as a linear quiz, no exploration.

## Credit and status

This is an **unofficial learning project**. It is not affiliated with, endorsed by, or produced by the Institute of Digital Government, MDDI, or the Singapore Government.

The frameworks, quoted passages and the health appointment booking case study are IDG's, reproduced here for study and linked back to source throughout. The story, characters and code are not theirs — any clumsiness in them is mine.
