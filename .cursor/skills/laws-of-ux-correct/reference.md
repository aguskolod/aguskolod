# Laws of UX — reference for correction

Source: [lawsofux.com](https://lawsofux.com/) (Jon Yablonski). Use this file while running `laws-of-ux-correct`.

For each law: definition, official takeaways, **fail signals** (code + visual), **fix steps** for the agent.

## Aesthetic-Usability Effect

- **ID:** `aesthetic-usability-effect`
- **Definition:** Users often perceive aesthetically pleasing design as design that’s more usable.
- **Source:** https://lawsofux.com/aesthetic-usability-effect
- **Official takeaways:**
  - An aesthetically pleasing design creates a positive response in people’s brains and leads them to believe the design actually works better.
  - People are more tolerant of minor usability issues when the design of a product or service is aesthetically pleasing.
  - Visually pleasing design can mask usability problems and prevent issues from being discovered during usability testing.
- **Fail if:**
  - Visual: inconsistent spacing, weak hierarchy, clashing type, muddy contrast, unfinished look that undermines trust
  - Code: ad-hoc colors/fonts not from a system; decorative noise fighting the CTA
- **Fix (agent instructions):**
  1. Align type scale, spacing rhythm, and palette to the approved direction tokens
  2. Remove visual noise competing with primary actions
  3. Do NOT use beauty to hide broken flows—still fix real usability issues

## Choice Overload

- **ID:** `choice-overload`
- **Definition:** The tendency for people to get overwhelmed when they are presented with a large number of options, often used interchangeably with the term paradox of choice.
- **Source:** https://lawsofux.com/choice-overload
- **Official takeaways:**
  - Too many options hurts users’ decision-making ability. How they feel about the experience as a whole can be significantly impacted as a result.
  - When comparison is necessary, we can avoid choice overload by enabling side-by-side comparison of related items and options that require a decision (e.g. pricing tiers).
  - We can avoid choice overload by optimizing our designs for the decision-making process and avoid overwhelming users by prioritizing the content that’s shown to them at any given moment (e.g. featured product), providing tools for narrowing down choices up front (e.g. search and filtering).
- **Fail if:**
  - Visual/code: many equal-weight CTAs, service cards, or nav items with no recommended path
  - Pricing or plan grids without highlight/default
- **Fix (agent instructions):**
  1. Keep one primary CTA style; demote others to text/outline
  2. Feature one recommended option; add filters/progressive disclosure if many items
  3. Cut or group secondary offers off the first viewport

## Chunking

- **ID:** `chunking`
- **Definition:** A process by which individual pieces of an information set are broken down and then grouped together in a meaningful whole.
- **Source:** https://lawsofux.com/chunking
- **Official takeaways:**
  - Chunking enables users to easily scan content. It allows them to easily identify the information that aligns with their goals and process that information to achieve their goals more quickly.
  - Structuring content into visually distinct groups with a clear hierarchy enables designers to align information with how people evaluate and process digital content.
  - Chunking can be used to help users understand underlying relationships by grouping content into distinctive modules, applying rules to separate content, and providing hierarchy.
- **Fail if:**
  - Long undifferentiated text walls; lists >~7 items without grouping
  - Sections without clear visual modules/hierarchy
- **Fix (agent instructions):**
  1. Split into labeled sections/cards with headings
  2. Group related items (3–5 per cluster) with spacing/borders
  3. Use scannable bullets and short paragraphs

## Cognitive Bias

- **ID:** `cognitive-bias`
- **Definition:** A systematic error of thinking or rationality in judgment that influence our perception of the world and our decision-making ability.
- **Source:** https://lawsofux.com/cognitive-bias
- **Official takeaways:**
  - Rather than thinking through every situation, we conserve mental energy by developing rules of thumb to make decisions which are based on past experiences. These mental shortcuts increase our efficiency by enabling us to make quick decisions without the need to thoroughly analyze a situation but can also influence our decision-making processes and judgement without our awareness.
  - Understanding of our own intrinsic biases may not eliminate them completely from our decision-making but it increases the chance that we can identify them in ourselves and others and serve as a safeguard against fallacious reasoning, unintentional discrimination or costly mistakes our decisions.
  - Take for example our tendency to seek out, interpret, and recall information in a way that confirms their preconceived notions and ideas. This is known as confirmation bias, and it can make having a logical discussion about a polarizing hot-button issue with someone incredibly difficult.
- **Fail if:**
  - Dark patterns: fake urgency, misleading hierarchy, disguised ads
  - Design assumes users will carefully read fine print
- **Fix (agent instructions):**
  1. Make primary path honest and obvious; disclose caveats near the action
  2. Use defaults that help the user goal, not trap them
  3. Test copy for unintended framing (scarcity without evidence → remove)

## Cognitive Load

- **ID:** `cognitive-load`
- **Definition:** The amount of mental resources needed to understand and interact with an interface.
- **Source:** https://lawsofux.com/cognitive-load
- **Official takeaways:**
  - When the amount of information coming in exceeds the space we have available, we struggle mentally to keep up — tasks become more difficult, details are missed, and we begin to feel overwhelmed.
  - Intrinsic cognitive load refers to the effort required by users to carry around information relevant to their goal, absorb new information and keep track of their goals.
  - Extraneous cognitive load refers to the mental processing that takes up resources but doesn't help users understand the content of an interface (e.g. distracting or unnecessary design elements).
- **Fail if:**
  - Too many simultaneous tasks, jargon, competing animations, dense forms
  - No progressive disclosure for complex flows
- **Fix (agent instructions):**
  1. Remove non-essential chrome; one job per section
  2. Split multi-step forms; hide advanced options until needed
  3. Replace jargon with visitor language from discovery/VoC

## Doherty Threshold

- **ID:** `doherty-threshold`
- **Definition:** Productivity soars when a computer and its users interact at a pace (<400ms) that ensures that neither has to wait on the other.
- **Source:** https://lawsofux.com/doherty-threshold
- **Official takeaways:**
  - Provide system feedback within 400 ms in order to keep users’ attention and increase productivity.
  - Use perceived performance to improve response time and reduce the perception of waiting.
  - Animation is one way to visually engage people while loading or processing is happening in the background.
  - Progress bars help make wait times tolerable, regardless of their accuracy.
  - Purposefully adding a delay to a process can actually increase its perceived value and instill a sense of trust, even when the process itself actually takes much less time.
- **Fail if:**
  - Interactions feel idle >~400ms with no feedback (spinners, skeletons, optimistic UI)
  - Heavy JS blocking first paint / TTI on mobile
- **Fix (agent instructions):**
  1. Add immediate feedback on click (pressed state, spinner, disable double-submit)
  2. Optimize LCP/CLS; defer non-critical scripts
  3. Show skeleton/placeholder for async content

## Fitts’s Law

- **ID:** `fittss-law`
- **Definition:** The time to acquire a target is a function of the distance to and size of the target.
- **Source:** https://lawsofux.com/fittss-law
- **Official takeaways:**
  - Touch targets should be large enough for users to accurately select them.
  - Touch targets should have ample spacing between them.
  - Touch targets should be placed in areas of an interface that allow them to be easily acquired.
- **Fail if:**
  - Tap targets <44×44px; cramped links; primary CTA far from thumb zone / attention
  - Adjacent targets without spacing causing mis-taps
- **Fix (agent instructions):**
  1. Enlarge primary buttons; min ~44px height on mobile
  2. Add gap between tappable items
  3. Place primary CTA near content focus / easy reach (sticky bar only if it doesn't cover content)

## Flow

- **ID:** `flow`
- **Definition:** The mental state in which a person performing some activity is fully immersed in a feeling of energized focus, full involvement, and enjoyment in the process of the activity.
- **Source:** https://lawsofux.com/flow
- **Official takeaways:**
  - Flow occurs when there is a balance between the difficulty of a task with the level of skill at the given task. It’s characterized by intense and focused concentration on the present, combined with a sense of total control.
  - A task that’s too difficult leads to heighten frustration while a task that’s too easy can lead to boredom. Finding the right balance requires matching the challenge with skill of the user.
  - Design for flow by providing the necessary feedback so that the user know what action has been done and what has been accomplished.
  - Optimize for efficiency and system responsiveness by removing any unnecessary friction, and making content and features available for discovery to avoid disengagement with the interface.
- **Fail if:**
  - Interruptions: popups, cookie walls mid-task, unexpected navigation resets
  - Inconsistent interaction patterns that break concentration
- **Fix (agent instructions):**
  1. Defer non-critical modals until after primary task or idle
  2. Keep scroll position/state; avoid full-page reloads for small actions
  3. Match motion intensity to direction.md (don't over-animate)

## Goal-Gradient Effect

- **ID:** `goal-gradient-effect`
- **Definition:** The tendency to approach a goal increases with proximity to the goal.
- **Source:** https://lawsofux.com/goal-gradient-effect
- **Official takeaways:**
  - The closer users are to completing a task, the faster they work towards reaching it.
  - Providing artificial progress towards a goal will help to ensure users are more likely to have the motivation to complete that task.
  - Provide a clear indication of progress in order to motivate users to complete tasks.
- **Fail if:**
  - Multi-step flows with no progress indicator or sense of remaining steps
  - Checkout/contact funnel feels endless
- **Fix (agent instructions):**
  1. Add step progress (e.g. 2 of 3) and clear 'almost done' near the end
  2. Show completion state after CTA success
  3. Shorten steps; front-load easy actions

## Hick’s Law

- **ID:** `hicks-law`
- **Definition:** The time it takes to make a decision increases with the number and complexity of choices.
- **Source:** https://lawsofux.com/hicks-law
- **Official takeaways:**
  - Minimize choices when response times are critical to decrease decision time.
  - Break complex tasks into smaller steps in order to decrease cognitive load.
  - Avoid overwhelming users by highlighting recommended options.
  - Use progressive onboarding to minimize cognitive load for new users.
  - Be careful not to simplify to the point of abstraction.
- **Fail if:**
  - Decision-critical UI with many parallel choices (nav mega-menus, 4+ filled buttons)
  - Complex first-run requiring many settings before value
- **Fix (agent instructions):**
  1. Reduce concurrent choices; highlight one recommended path
  2. Break decisions into sequential steps
  3. Don't oversimplify into vague icons without labels

## Jakob’s Law

- **ID:** `jakobs-law`
- **Definition:** Users spend most of their time on other sites. This means that users prefer your site to work the same way as all the other sites they already know.
- **Source:** https://lawsofux.com/jakobs-law
- **Official takeaways:**
  - Users will transfer expectations they have built around one familiar product to another that appears similar.
  - By leveraging existing mental models, we can create superior user experiences in which the users can focus on their tasks rather than on learning new models.
  - When making changes, minimize discord by empowering users to continue using a familiar version for a limited time.
- **Fail if:**
  - Novel patterns for standard jobs (weird nav, unconventional form controls) without teaching
  - Logo not linking home; search/cart/phone in unexpected places for the category
- **Fix (agent instructions):**
  1. Use conventional placements for nav, logo→home, phone/WhatsApp CTAs on local sites
  2. Reserve innovation for brand expression, not core interaction models
  3. If breaking convention, add clear labels and affordances

## Law of Common Region

- **ID:** `law-of-common-region`
- **Definition:** Elements tend to be perceived into groups if they are sharing an area with a clearly defined boundary.
- **Source:** https://lawsofux.com/law-of-common-region
- **Official takeaways:**
  - Common region creates a clear structure and helps users quickly and effectively understand the relationship between elements and sections.
  - Adding a border around an element or group of elements is an easy way to create common region.
  - Common region can also be created by defining a background behind an element or group of elements.
- **Fail if:**
  - Related items not sharing a visible region; unrelated items boxed together
- **Fix (agent instructions):**
  1. Wrap related content in a shared background/card/bordered region
  2. Separate unrelated blocks with clear region boundaries

## Law of Prägnanz

- **ID:** `law-of-pragnanz`
- **Definition:** People will perceive and interpret ambiguous or complex images as the simplest form possible, because it is the interpretation that requires the least cognitive effort of us.
- **Source:** https://lawsofux.com/law-of-pr%C3%A4gnanz
- **Official takeaways:**
  - The human eye likes to find simplicity and order in complex shapes because it prevents us from becoming overwhelmed with information.
  - Research confirms that people are better able to visually process and remember simple figures than complex figures.
  - The human eye simplifies complex shapes by transforming them into a single, unified shape.
- **Fail if:**
  - Ambiguous icons, cluttered overlays, shapes that don't read as simple forms
  - Low-contrast text over busy images
- **Fix (agent instructions):**
  1. Simplify composition; add text labels to icons
  2. Increase contrast overlays; reduce competing decorative layers

## Law of Proximity

- **ID:** `law-of-proximity`
- **Definition:** Objects that are near, or proximate to each other, tend to be grouped together.
- **Source:** https://lawsofux.com/law-of-proximity
- **Official takeaways:**
  - Proximity helps to establish a relationship with nearby objects.
  - Elements in close proximity are perceived to share similar functionality or traits.
  - Proximity helps users understand and organize information faster and more efficiently.
- **Fail if:**
  - Labels far from inputs; captions far from images; CTA far from its supporting proof
  - Spacing implies wrong grouping
- **Fix (agent instructions):**
  1. Tighten space within a group; increase space between groups
  2. Place label adjacent to control; CTA next to its offer copy

## Law of Similarity

- **ID:** `law-of-similarity`
- **Definition:** The human eye tends to perceive similar elements as a complete picture, shape, or group, even if those elements are separated.
- **Source:** https://lawsofux.com/law-of-similarity
- **Official takeaways:**
  - Elements that are visually similar will be perceived as related.
  - Color, shape, and size, orientation and movement can signal that elements belong to the same group and likely share a common meaning or functionality.
  - Ensure that links and navigation systems are visually differentiated from normal text elements.
- **Fail if:**
  - Same-looking elements behave differently; different actions share identical styles
  - Inconsistent button/link styling
- **Fix (agent instructions):**
  1. One visual language per role (primary/secondary/text link)
  2. Don't style unrelated items identically

## Law of Uniform Connectedness

- **ID:** `law-of-uniform-connectedness`
- **Definition:** Elements that are visually connected are perceived as more related than elements with no connection.
- **Source:** https://lawsofux.com/law-of-uniform-connectedness
- **Official takeaways:**
  - Group functions of a similar nature so they are visually connected via colors, lines, frames, or other shapes.
  - Alternately, you can use a tangible connecting reference (line, arrow, etc) from one element to the next to also create a visual connection.
  - Use uniform connectedness to show context or to emphasize the relationship between similar items.
- **Fail if:**
  - Steps or related actions lack connecting lines/timeline/shared container when relationship matters
- **Fix (agent instructions):**
  1. Connect process steps with a line/timeline or numbered sequence in one region
  2. Use shared borders/backgrounds for related controls

## Mental Model

- **ID:** `mental-model`
- **Definition:** A compressed model based on what we think we know about a system and how it works.
- **Source:** https://lawsofux.com/mental-model
- **Official takeaways:**
  - We form a working model in our minds around what we think we know about a system, especially about how it works, and then we apply that model to new situations where the system is similar.
  - Match designs to the users’ mental models to improve their experience. This enables them to easily transfer their knowledge from one product or experience to another, without the need to first take the time to understand how the new system works.
  - Good user experiences are made possible when the design of a product or service is in alignment with the user’s mental model. Take for example e-commerce websites, which use consistent patterns and conventions such product cards, virtual carts and checkout flows in order to conform to users’ expectations.
  - The task of shrinking the gap between our own mental models and those of the users is one of the biggest challenges we face, and to achieve this goal we use a variety of user research methods (e.g. user interviews, personas, journey maps, empathy maps).
- **Fail if:**
  - UI contradicts how users expect the domain to work (e.g. local business without phone CTA)
  - Labels that don't match user language
- **Fix (agent instructions):**
  1. Align structure and CTAs with category norms + discovery VoC
  2. Rename controls to match user mental model; add brief explanation only if needed

## Miller’s Law

- **ID:** `millers-law`
- **Definition:** The average person can only keep 7 (plus or minus 2) items in their working memory.
- **Source:** https://lawsofux.com/millers-law
- **Official takeaways:**
  - Don’t use the “magical number seven” to justify unnecessary design limitations.
  - Organize content into smaller chunks to help users process, understand, and memorize easily.
  - Remember that short-term memory capacity will vary per individual, based on their prior knowledge and situational context.
- **Fail if:**
  - Asking users to remember many items across screens; huge unchunked menus
  - Misusing 'max 7 nav items' as a hard superstition while leaving content unchunked
- **Fix (agent instructions):**
  1. Chunk content; don't force memorization—keep key info visible
  2. Organize menus into groups; avoid arbitrary 7-item caps when IA needs more

## Occam’s Razor

- **ID:** `occams-razor`
- **Definition:** Among competing hypotheses that predict equally well, the one with the fewest assumptions should be selected.
- **Source:** https://lawsofux.com/occams-razor
- **Official takeaways:**
  - The best method for reducing complexity is to avoid it in the first place.
  - Analyze each element and remove as many as possible, without compromising the overall function.
  - Consider completion only when no additional items can be removed.
- **Fail if:**
  - Over-engineered UI for a simple job; redundant sections saying the same thing
- **Fix (agent instructions):**
  1. Remove duplicate sections/CTAs; simplest structure that achieves the goal
  2. Prefer one clear path over multiple clever alternatives

## Paradox of the Active User

- **ID:** `paradox-of-the-active-user`
- **Definition:** Users never read manuals but start using the software immediately.
- **Source:** https://lawsofux.com/paradox-of-the-active-user
- **Official takeaways:**
  - Users are often motivated to complete their immediate tasks and therefore they don't want to spend time up front reading documentation.
  - This paradox exist because users will save time in the long term if they take the time to optimize the system and learn more about it.
  - Make guidance accessible throughout the product experience and design it to fit within the context of use so that it can help these active new users no matter what path they choose to take (e.g. tooltips with helpful information).
- **Fail if:**
  - Critical info only in long intros/tooltips users skip; blocked behind 'learn more'
  - Onboarding walls before first success
- **Fix (agent instructions):**
  1. Make the product usable without reading manuals—inline cues, defaults, empty states that teach by doing
  2. Put must-know constraints near the action, not only in FAQ

## Pareto Principle

- **ID:** `pareto-principle`
- **Definition:** The Pareto principle states that, for many events, roughly 80% of the effects come from 20% of the causes.
- **Source:** https://lawsofux.com/pareto-principle
- **Official takeaways:**
  - Inputs and outputs are often not evenly distributed.
  - A large group may contain only a few meaningful contributors to the desired outcome.
  - Focus the majority of effort on the areas that will bring the largest benefits to the most users.
- **Fail if:**
  - Equal visual weight for rare and common actions; burying the primary conversion
- **Fix (agent instructions):**
  1. Invest layout/emphasis in the ~20% of actions that drive ~80% of outcomes (primary CTA, core offer)
  2. Demote edge-case links to footer/secondary

## Parkinson’s Law

- **ID:** `parkinsons-law`
- **Definition:** Any task will inflate until all of the available time is spent.
- **Source:** https://lawsofux.com/parkinsons-law
- **Official takeaways:**
  - Limit the time it takes to complete a task to what users expect it’ll take.
  - Reducing the actual duration to complete a task from the expected duration will improve the overall user experience.
  - Leverage features such as autofill to save the user time when providing critical information within forms. This allows for quick completion of purchases, bookings and other such functions while preventing task inflation.
- **Fail if:**
  - Forms/flows that expand to fill space with optional fields by default
  - Unconstrained multi-page wizards
- **Fix (agent instructions):**
  1. Show only required fields; progressive disclose optionals
  2. Timebox steps; remove vanity questions

## Peak-End Rule

- **ID:** `peak-end-rule`
- **Definition:** People judge an experience largely based on how they felt at its peak and at its end, rather than the total sum or average of every moment of the experience.
- **Source:** https://lawsofux.com/peak-end-rule
- **Official takeaways:**
  - Pay close attention to the most intense points and the final moments (the “end”) of the user journey.
  - Identify the moments when your product is most helpful, valuable, or entertaining and design to delight the end user.
  - Remember that people recall negative experiences more vividly than positive ones.
- **Fail if:**
  - Strong hero but weak/broken ending (dead footer CTA, error on submit, abrupt stop)
  - Peak moment is a frustrating paywall/error
- **Fix (agent instructions):**
  1. Design a strong closing CTA/success state
  2. Fix end-of-flow errors; make confirmation reassuring
  3. Ensure the emotional peak (offer/proof) isn't undercut by a poor ending

## Postel’s Law

- **ID:** `postels-law`
- **Definition:** Be liberal in what you accept, and conservative in what you send.
- **Source:** https://lawsofux.com/postels-law
- **Official takeaways:**
  - Be empathetic to, flexible about, and tolerant of any of the various actions the user could take or any input they might provide.
  - Anticipate virtually anything in terms of input, access, and capability while providing a reliable and accessible interface.
  - The more we can anticipate and plan for in design, the more resilient the design will be.
  - Accept variable input from users, translating that input to meet your requirements, defining boundaries for input, and providing clear feedback to the user.
- **Fail if:**
  - Strict input formats (phone/email) with hostile errors; brittle parsers
  - Output inconsistent (weird date formats, unclear messages)
- **Fix (agent instructions):**
  1. Accept flexible input (spaces in phone, common email typos guidance); normalize on submit
  2. Be conservative/clear in what you display and send

## Selective Attention

- **ID:** `selective-attention`
- **Definition:** The process of focusing our attention only to a subset of stimuli in an environment — usually those related to our goals.
- **Source:** https://lawsofux.com/selective-attention
- **Official takeaways:**
  - People often filter out information that isn’t relevant. This happens in order to maintain focus on information that is important or relevant to the task at hand. Designers must guide users’ attention, prevent them from being overwhelmed or distracted, and help them find relevant information or action.
  - Banner Blindness is an example phenomenon of selection attention where visitors to a website consciously or unconsciously ignore banner-like information. Users have learned to ignore content that resembles ads, is close to ads, or appears in locations traditionally dedicated to ads. Avoid confusion by not styling content to look like ads or placing content and ads in the same visual section.
  - Change blindness is another example phenomenon of selection attention that occurs when significant changes in an interface go unnoticed because due to the limitations of human attention and the lack of strong cues. Avoid this by analyzing your design for any competing changes that may happen at the same time and that may divert attention from each other.
- **Fail if:**
  - Banner blindness triggers: everything looks like an ad; critical info in ignored sidebars
  - Motion/ads stealing attention from the goal
- **Fix (agent instructions):**
  1. Place goal-critical content in expected focal areas; reduce ad-like styling on real content
  2. Limit motion near primary CTA

## Serial Position Effect

- **ID:** `serial-position-effect`
- **Definition:** Users have a propensity to best remember the first and last items in a series.
- **Source:** https://lawsofux.com/serial-position-effect
- **Official takeaways:**
  - Placing the least important items in the middle of lists can be helpful because these items tend to be stored less frequently in long-term and working memory.
  - Positioning key actions on the far left and right within elements such as navigation can increase memorization.
- **Fail if:**
  - Most important items buried in the middle of lists/nav/pricing
- **Fix (agent instructions):**
  1. Put key items first and/or last in lists and sections
  2. Hero (start) and final CTA (end) carry the core message

## Tesler’s Law

- **ID:** `teslers-law`
- **Definition:** Tesler's Law, also known as The Law of Conservation of Complexity, states that for any system there is a certain amount of complexity which cannot be reduced.
- **Source:** https://lawsofux.com/teslers-law
- **Official takeaways:**
  - All processes have a core of complexity that cannot be designed away and therefore must be assumed by either the system or the user.
  - Ensure as much as possible of the burden is lifted from users by dealing with inherent complexity during design and development.
  - Remember to not build products and services for an idealized, rational user, because people don’t always behave rationally in real life.
  - Make guidance accessible and fit within the context of use so that it can help these active new users, no matter what path they choose to take (e.g., tooltips with helpful information).
- **Fail if:**
  - Pushing irreducible complexity onto the user (raw config, unexplained choices)
  - Fake simplicity that hides needed controls until too late
- **Fix (agent instructions):**
  1. Absorb complexity in the system (smart defaults, progressive disclosure)
  2. Don't delete necessary complexity—relocate it away from the critical path

## Von Restorff Effect

- **ID:** `von-restorff-effect`
- **Definition:** The Von Restorff effect, also known as The Isolation Effect, predicts that when multiple similar objects are present, the one that differs from the rest is most likely to be remembered.
- **Source:** https://lawsofux.com/von-restorff-effect
- **Official takeaways:**
  - Make important information or key actions visually distinctive.
  - Use restraint when placing emphasis on visual elements to avoid them competing with one another and to ensure salient items don’t get mistakenly identified as ads.
  - Don’t exclude those with a color vision deficiency or low vision by relying exclusively on color to communicate contrast.
  - Carefully consider users with motion sensitivity when using motion to communicate contrast.
- **Fail if:**
  - Primary CTA doesn't visually isolate from surroundings
  - Too many 'unique' accents so nothing stands out
- **Fix (agent instructions):**
  1. Make one element distinctly different for the primary action/highlight
  2. Reduce competing accents so isolation works

## Working Memory

- **ID:** `working-memory`
- **Definition:** A cognitive system that temporarily holds and manipulates information needed to complete tasks.
- **Source:** https://lawsofux.com/working-memory
- **Official takeaways:**
  - Working memory is limited to 4-7 chunks of information at any given moment with each chunk fades after 20-30 seconds. We use it to keep track of information in order to achieve tasks but we often have trouble remembering what information we’ve already seen. Designers must be mindful of this limit when displaying information to users and ensure it’s both necessary and relevant.
  - Our brains are good at recognizing something we’ve seen before but not at keeping new information ready to be used. We can support recognition over recall by making it clear what information has already been viewed (e.g. visually differentiating visited links and providing breadcrumbs links).
  - Place burden of memory on the system, not the user. We can lessen the burden of memorizing critical information by carrying it over from screen to screen when necessary (e.g. comparison tables that make comparing multiple items easy).
- **Fail if:**
  - Users must remember info from earlier steps (codes, prices) not shown again
  - Multi-step compare without sticky summary
- **Fix (agent instructions):**
  1. Keep relevant context on-screen; repeat key facts near decisions
  2. Provide summary sidebars/sticky bars for multi-step tasks

## Zeigarnik Effect

- **ID:** `zeigarnik-effect`
- **Definition:** People remember uncompleted or interrupted tasks better than completed tasks.
- **Source:** https://lawsofux.com/zeigarnik-effect
- **Official takeaways:**
  - Invite content discovery by providing clear signifiers of additional content.
  - Providing artificial progress towards a goal will help to ensure users are more likely to have the motivation to complete that task.
  - Provide a clear indication of progress in order to motivate users to complete tasks.
- **Fail if:**
  - Abandoned incomplete tasks with no save/resume/progress reminder when completion matters
- **Fix (agent instructions):**
  1. Show incomplete progress; allow resume; gentle reminders for unfinished high-value tasks
  2. Don't exploit anxiety dark-pattern style—use for helpful completion

