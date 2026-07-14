Here is how I would approach the content management and documentation issues from the given list.

[TOC]

## **Step 0. Inventory and planning**

Better planned roadmap and structured changes eventually bring more value than chaotic immediate action. Especially in large ecosystems. The investigation and preparation takes time but it would help us understand the scope of required changes and identify real causes of existing issues.

Within this step, I would:

- make an **inventory of target documentation, data, and metrics**;
- make a table with different documented sections with their owners, and received feedback;
- prepare action plan and involve other stakeholders.

## **Step 1. Standardization and Single-Source-of-Truth**

From the given list, I would start from addressing the inconsistency in terminology and metric definitions as it is the high-impact issue. **Standardization and implementing the single-source-of-truth approach** in the department would also solve most of the problems that employees are currently facing.

If different teams maintain the documentation independently, then it is time to bring them together and align the way-of-working. Considering that documentation quality varies, a simple solution is to take the best parts of the documentation as a standard and apply it to other sections. The process with the agreed standard should be documented and communicated to the contributing teams. It would be beneficial to organize 2-3 workshops to kick off the standardization and clean-up processes.

!!! warning

    These type of documentation improvements are good and should be met positively among contributors. However, in some cases, standardization creates tension between the teams. Considering that eventually we need to decide on ONE solution and deprecate or rewrite the work of other teams, we would need to think of ways to preserve good team dynamics and not let involved parties feel discouraged or left out. 
    
    If alignment of the teams is problematic, the proposed changes should be communicated to the teams by higher management.

## **Step 2. Feedback loops in the chat**

As a next step, I would address the frequent questions in the chat as it is a low hanging fruit.

I personally think that a technical writer should be an active member of internal chats and forums related to their features/docs. Forums and chats are a great source of feedback and a way to connect with users.

Instead of explaining the same things again in the chats, the team should quickly write/update their docs and send a link to the documentation.

To make this sustainable, it helps to introduce a simple rule: if a question appears repeatedly in chat, create or update a doc page within a fixed time period (for example, within 2 working days).

## **Step 3. Addressing poor discoverability**

From my experience, poor documentation discoverability might be caused by various factors:

- Documentation is not properly structured.
- There are several versions of the same instructions.
- Documentation is outdated.
- Issues with the tooling (for example, no proper search engine in docs-as-code stack; "trashed" search results on the website or Confluence space with a lot of outdated documentation).

The implementation order inside this step can be:

1. Identify duplicate or conflicting pages and mark one as canonical.
2. Improve information architecture (navigation, page titles, tags, cross-links).
3. Archive or at least label outdated pages.
4. Tune search (metadata, synonyms for key business terms, indexing rules).
5. [Optional] After cleaning up the data, it can be worthy to invest in a **vector search engine** (semantic or similarity search). The vector search database can be later used for implementing the **Ask AI** feature. A simple semantic search can be built using open-source solutions. I have experience with **Qdrant**-based search, and the implementation was not difficult. However, it requires a server for the engine and the vector DB.

!!! info
    
    This step partially intersects with Step 1. Labelling outdated pages and improving information architecture can be done in parallel within organized workshops.

## **Step 4. Governance**

After the new processes are established and documented, we need mechanisms to make sure they are implemented. This can include:

- Ownership per documentation domain or per metric area.
- A lightweight review workflow for metric-related changes (for example, approval from a writer from another domain or data owner).
- Documentation quality checks in CI (broken links, metadata, required sections).
- A recurring content health review (quarterly).

!!! warning

    Stronger governance improves consistency, but it also adds process overhead. So, I would go with a lightweight model at the beginning.

## **How to measure success**

We can use the following KPIs to measure the results:

- There is a clearly documented process of documenting metrics.
- There is a clear ownership of documentation sections.
- Reduced number of inconsistent definitions and duplicate pages.
- Reduced number of repeated questions about metrics in chats.
- Faster update time between a metric change and documentation update.
- Regular feedback from documentation users collected in surveys or interviews.

## **[Optional] Treating metrics as code or variables**

Modern docs-as-code frameworks support data and variables (for example, `Jinja2` integration in `Material for MkDocs`, data files in `Hugo`, `.mdx`). In some cases, you can treat terminology and metric names as structured data and keep them in a separate repository (or in a dedicated data layer in the docs repo).

By storing metric definitions and terminology as structured data, the team can automate part of governance: enforce canonical terms, reuse approved metric definitions across pages, and run CI checks that detect deviations before publishing.

Making a decision on this approach requires good knowledge of the internal documentation and metrics. I would need to make an inventory of target data and metrics to understand if this approach is applicable to the provided documentation. I would guess that you already have an established process and way of working for documenting metrics: whether data metrics are invoked/extracted from the code, declared as variables, or hardcoded in the documentation.

!!! warning

    This approach might be costly because it requires major changes in the process of documenting metrics. It might be worth it to investigate and test it if the team already implemented the measures mentioned above. The team should work on this approach only if there is an actual business need for it.
