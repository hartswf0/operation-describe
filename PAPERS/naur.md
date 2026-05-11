## Theory, Practice, Victory

### Software Development After Naur, Ehn, and Musashi

### Abstract

Software development is still too often governed by a production fantasy: the belief that the essence of programming lies in producing code, documents, specifications, diagrams, and processes that can be handed from one group to another as if understanding were a transferable object. Peter Naur’s theory-building view of programming breaks that fantasy. A program, for Naur, is not primarily a text but a living theory held by programmers who understand how the program maps onto the world, why its parts are shaped as they are, and how it can be modified without destroying its inner coherence. Pelle Ehn extends this argument into the field of participatory design, showing that understanding does not emerge from detached description but from shared practice, mockups, language-games, and design-by-doing. Musashi supplies the severe pragmatic discipline: use any tool, become attached to none, cut waste, observe reflectively, and win. Together, Naur, Ehn, and Musashi form a theory of software practice in which the central problem is not method selection but the survival of shared practical judgment. The opponent is not the user, the teammate, the manager, or the organization. The opponent is the problem. There is only us.

---

## 1. The Production Lie

Software development keeps trying to pretend that it is an industrial process. It wants to believe that programs are products, programmers are interchangeable labor units, requirements are captured facts, methods are repeatable machines, and documentation is the container of understanding. This fantasy is administratively convenient. It allows organizations to imagine that knowledge can be stored, transferred, audited, and replaced without serious loss. It turns software into a factory problem.

Peter Naur’s “Programming as Theory Building” is devastating because it says: no. That is not what programming is.

Programming is not the production of code. Code is one residue of programming. Documentation is another residue. Diagrams, specifications, tickets, comments, tests, and procedures are all residues. They matter, but they are not the thing itself. The thing itself is the programmer’s possession of a theory: a living understanding of how some part of the world can be supported, represented, transformed, or coordinated by a program.

This is not “theory” in the weak academic sense of abstract explanation floating above practice. Naur draws from Gilbert Ryle’s distinction between knowing-that and knowing-how. A person has a theory when they can act intelligently, explain what they are doing, justify choices, answer questions, recognize relevant similarities, and respond to new situations. A programmer who has the theory of a program does not merely know where the files are. They know why the structure is shaped as it is. They know which possible changes would harmonize with the system and which would wound it. They can feel when a proposed modification is a natural extension and when it is a patch that will begin the slow rot.

This is why software so often decays after handoff. The text remains, but the theory leaves.

A dead program can still run. It can still produce correct outputs. It can still serve users. But for Naur, a program dies when the people who possess its theory are no longer in active control of it. Death becomes visible only when modification is required. The system can execute, but it can no longer intelligently change. It becomes a machine without a living interpreter.

This single claim should reorder how we think about maintenance, documentation, onboarding, architecture, technical debt, and software process. The central question is not: “Have we documented the system?” The central question is: “Can another competent person build the theory required to change this system well?”

Most documentation fails because it aims to preserve facts instead of cultivating theory. It names parts. It records decisions. It sketches structures. But it often does not help the next programmer understand what the system is trying to be, how the world appears inside it, what kinds of changes it welcomes, and what kinds of changes would betray its form.

The cruelest illusion in software management is that a program can be transferred by transferring its artifacts. Naur says that this is false. The theory is embodied in people. Therefore, passing a program on requires apprenticeship, conversation, shared modification, guided practice, and exposure to the real world activity the program serves. It requires a living lineage.

The code is not enough. The document is not enough. The diagram is not enough. The method is not enough.

The theory must be rebuilt in another mind.

---

## 2. Program Life, Program Death

Naur’s strongest contribution is not simply that programmers know more than they can write down. Many people know this casually. His stronger claim is that this unwritten knowledge is not peripheral. It is the primary substance of programming.

This changes the meaning of program life.

A program is alive when the team responsible for it possesses the theory required to modify it coherently. A program is dying when modification is still possible but increasingly takes the form of defensive patching, local fixes, duplicated logic, inconsistent naming, and structural evasions. A program is dead when no one can explain how the program’s parts relate to the world it serves, why the program is organized as it is, or how a new demand should be absorbed without damage.

The signs of program death are familiar. A feature is added in the wrong layer because nobody remembers why the layer exists. A workaround becomes permanent because the underlying model is feared. A new module duplicates an old capability because the old capability is illegible. Tests are added around confusion, not understanding. Documentation grows while confidence shrinks. The team says, “Don’t touch that part.” The system still runs, but nobody trusts it.

This is not merely “technical debt.” Technical debt is often used as a metaphor for mess. Naur allows a sharper diagnosis: program decay is theory loss made visible in text.

The decayed program contains the fossil traces of earlier intelligence. The original structure may still be visible, but it no longer governs change. Later additions cling to it like barnacles. The system becomes a record of successive programmers solving local problems without possessing the larger theory that would let those solutions converge.

This has a brutal implication: revival may be more expensive than replacement. If the original theory is gone, a new team must reconstruct a theory from artifacts never capable of containing it fully. They must infer intention from structure, reconstruct world mappings from code, and decide which irregularities are meaningful and which are accidental. This is a strange kind of archaeology: the new programmers excavate not just what the old system does, but what its makers understood.

Naur warns that this revival is strictly impossible if understood as recovering the original theory exactly from documentation alone. A new theory can be built, but it may not be the same theory. It may fit the text awkwardly. The programmer may feel torn between loyalty to the existing code and loyalty to the new understanding forming in their own mind. Anyone who has inherited a large codebase knows this sensation: the old program makes demands, but it does not explain itself.

The managerial lesson is uncomfortable. If organizations want living software, they must preserve living theory. That means preserving continuity of understanding, not merely continuity of files. It means making handoff a social and practical process. It means treating experienced programmers not as replaceable operators but as stewards of a theory that gives the program its modifiability.

This is also why “clean code” is not merely aesthetic. Clear names, coherent structure, good boundaries, useful tests, and purposeful comments matter because they help another person build the theory. Clean code is not code that looks pretty. It is code that teaches its reader what kind of world it believes in.

---

## 3. The False Comfort of Method

Naur’s theory-building view also attacks the prestige of method.

A method promises order. It tells programmers what to do, when to do it, which artifacts to produce, which notation to use, which procedure to follow. Methods are seductive because they appear to make programming manageable from outside the programmer’s judgment. They promise that if the correct steps are followed, good software will result.

Naur does not deny that techniques can help. He denies that method can replace theory building.

The distinction matters. A notation, diagram, architecture pattern, testing discipline, modeling technique, or process ritual can support the formation of theory. It can provoke useful questions. It can expose contradiction. It can discipline attention. It can create shared vocabulary. But no method can determine in advance which aspects of the world matter, which similarities are relevant, which design choice is justified, or how a future modification should be integrated.

Those acts require judgment.

A programmer must decide what the method means here. The rule does not contain the intelligence for applying the rule. If it did, one would need another rule for how to apply that rule, and another for that rule, and so on. At the center of practice is not procedure but skilled judgment.

This does not make software development mystical. It makes it human.

The anti-method argument is not an argument for chaos. It is an argument against confusing the support structure with the work. A method can be valuable when it sharpens perception, coordinates attention, and helps people build shared theory. It becomes harmful when it lets the organization believe that following the method is equivalent to understanding the problem.

This is the difference between discipline and theater.

A disciplined team uses process as a tool. A theatrical team uses process as a costume. The disciplined team asks: did this help us understand, decide, build, test, and deliver? The theatrical team asks: did we perform the signs of seriousness?

Naur gives us the intellectual basis for distrusting process theater. If programming is theory building, then any process must be judged by whether it helps programmers and users form, share, test, and preserve the theory of the system. If it does not, it is decoration.

---

## 4. Ehn’s Turn: From Description to Practice

Pelle Ehn takes the argument into the workshop.

Where Naur asks what programmers possess when they understand a program, Ehn asks how designers and users can come to understand a future system together. His answer is Wittgensteinian: meaning is not secured by accurate description but by use within a form of life.

This is a direct attack on the requirements fantasy. Traditional systems development often assumes that users possess needs internally, that analysts can extract those needs through interviews, that descriptions can mirror reality, and that designers can implement the described system. Ehn says this misses the practical character of work.

Users often cannot fully state what they know because much of what they know exists as skill. The typographer knows how to crop a picture, balance a page, judge a layout, use a knife, sequence a task, and recognize when something is right. But this knowledge is not always available as propositions. It appears in action.

Ask the user to explain the work and you get one kind of knowledge. Watch the user do the work and you get another. Invite the user to act within a mockup of a possible future tool and you get something else again: practical imagination.

This is why Ehn’s design artifacts matter. Mockups, prototypes, scenarios, role-playing games, workplace visits, and organizational games are not crude versions of final systems. They are instruments for staging a language-game in which users and designers can act together. They allow tacit knowledge to surface without pretending it has become fully explicit. They let people test a future by rehearsing it.

The famous cardboard-box laser printer matters because it had no technical functionality and still functioned as a design artifact. It reminded typographers of older proof machines while suggesting a possible future practice. Its value did not lie in mirroring reality. Its value lay in the use it enabled inside a shared design game.

This is Ehn’s core move: a design artifact means by what it lets participants do.

A requirements document tries to say what the future system should be. A mockup lets people discover what the future system might mean in practice. The difference is enormous. The first privileges description. The second privileges situated action.

Ehn’s Wittgensteinian inheritance reframes design as the creation of new language-games. Designers and users do not simply exchange information. They learn how to participate in a shared activity where new tools, new words, new gestures, new expectations, and new forms of cooperation become possible. The designer’s role is not merely to represent user needs but to stage conditions under which users and designers can make sense together.

That staging is political. It decides whose skill counts. It decides whether users become sources of requirements or participants in invention. It decides whether the system will extend living practice or impose an alien structure upon it.

---

## 5. Skill, Participation, and the Limits of Formalization

Ehn’s deepest lesson is that participation without skill is hollow.

It is easy to say users should participate in design. It is harder to organize design so that their practical understanding actually has force. Many participatory processes become ceremonial. Users are invited to meetings, asked for opinions, shown diagrams, and then ignored by the deeper machinery of design. This is participation as legitimacy theater.

For Ehn, real participation requires a shared design language-game that has family resemblance to the users’ existing practices. Users must be able to bring their skill into the process. Designers must also participate in use, not merely observe from outside. The gap between designer and user is not closed by more accurate description. It is narrowed by shared doing.

This reverses the usual hierarchy of knowledge. Formal description is not the superior form into which practical knowledge must be translated. Practical understanding is not incomplete theory. It is a different kind of knowing, often richer than what can be said.

The typographer who can produce a balanced page may not be able to formalize all the rules of balance. The carpenter may not be able to fully specify the skilled use of every tool. The musician may not be able to describe the sound of a clarinet in propositions sufficient to teach hearing. The programmer may not be able to write down all the judgments that make a modification elegant rather than destructive.

This does not mean that language is useless. It means language works within practice. Words, diagrams, models, and descriptions matter when they serve as reminders, paradigm cases, provocations, and coordination devices. They help bring experience to mind. They do not replace experience.

Ehn’s emphasis on tradition and transcendence is crucial here. Design is not pure novelty. Creative change depends on inherited skill. One must know the rules of a practice in order to bend them intelligently. A tool that ignores existing practice may call itself revolutionary, but often it is merely incompetent. A tool that only preserves existing practice may be usable, but it may foreclose transformation.

The design problem is dialectical: preserve enough family resemblance for the new tool to make sense, while opening enough difference for practice to change.

This is why good design-by-doing is neither conservative nor reckless. It stages contact between the familiar and the possible. It lets users recognize their world and then see it otherwise.

---

## 6. The Shared Theory of the Team

Naur and Ehn converge on a single point: understanding is not transferred by artifact alone. It is cultivated through participation in practice.

For Naur, the programmer must build a theory of how the program supports the world. For Ehn, designers and users must create a language-game in which future use can be explored through action. Both reject the fantasy of complete formalization. Both insist that knowledge lives in skilled human activity. Both treat artifacts as aids to understanding, not replacements for understanding.

This convergence gives us a more powerful account of software teams.

A software team is not merely a group of individuals assigned to tasks. It is a theory-forming organism. Its health depends on whether its members can build compatible theories of the system, the world it serves, the tools they use, and the changes they are making. A team with no shared theory produces local cleverness and global incoherence. A team with shared theory can move quickly because each member’s decisions tend to harmonize with the others.

This is why metaphor can be powerful in software design. A good metaphor compresses a theory into a portable imaginative form. If a system is like an assembly line, a restaurant, a ledger, a newsroom, a map, a stage, or a garden, then the metaphor gives programmers a way to guess where new responsibilities belong, what kinds of interactions are natural, and what kinds of additions feel wrong.

The metaphor is not valuable because it is poetic. It is valuable because it coordinates expectation.

A good metaphor lets different people make similar guesses. It gives the team a shared direction without requiring every implication to be stated. It is documentation for the imagination. Like Ehn’s mockup, it works by triggering relevant experience. Like Naur’s theory, it helps programmers justify and modify.

But metaphors can also decay. A metaphor becomes dangerous when it is protected after it stops fitting. It becomes ideology. The team must remain free to revise or abandon it when the world pushes back.

This gives us a practical test for every software artifact: does it help the team build, share, test, or preserve theory?

If yes, keep it.

If no, cut it.

---

## 7. Musashi Against Process Theater

Musashi enters this lineage like a blade.

His contribution is not philosophical subtlety but pragmatic severity. Do not become attached to any weapon. Do not confuse showmanship with victory. Observe both the large picture and the small detail. Practice until principle becomes embodied, then detach from the principle. Use what works. Cut what does not. Win.

Translated into software, Musashi is an antidote to method worship.

Every software culture has schools: UML, RUP, CMM, XP, Scrum, Kanban, TDD, DDD, microservices, serverless, design systems, AI coding agents, formal methods, no-code tools, architecture frameworks, roadmapping rituals. Each school sees something. Each also blinds. Each has conditions under which it helps and conditions under which it becomes waste.

The Musashian software practitioner asks: what is the situation? What weapon is appropriate here? What can be discarded? What movement is useless? What would solve the problem directly?

This is not anti-intellectual. It is anti-attachment.

A team attached to a method will preserve the method even when it stops serving the work. A team trained in tool pluralism will pick up and put down techniques as needed. Sometimes a diagram is the right tool. Sometimes a test suite. Sometimes a prototype. Sometimes a conversation. Sometimes a rewrite. Sometimes a spreadsheet. Sometimes a whiteboard. Sometimes the correct move is to delete the meeting.

Musashi’s “win” must be translated carefully. In software, winning is not defeating people. The opponent is the problem: the obstacle preventing the delivery of a useful, working system. The user is not the opponent. The teammate is not the opponent. The manager is not the opponent. The sponsor is not the opponent. When teams misidentify the opponent, they turn inward and begin destroying their own capacity.

This is why Musashi must be humanized. In martial combat, the opponent is a person. In software development, the opponent is confusion, mismatch, delay, brittleness, fear, waste, misalignment, overproduction, under-learning, and incoherent change. To “cut down the opponent” is to remove the obstacle while keeping the people intact.

This leads to microtouch intervention.

The immature organization reaches for amputation: reorganize everything, impose a new framework, replace the toolchain, rewrite the system, add governance, fire people, add process, centralize authority. Sometimes structural replacement is necessary. But often the wiser move is smaller. Change seating. Clarify one decision boundary. Remove one useless approval. Put the user in the room. Rename a concept. Create a shared metaphor. Delete a stale artifact. Pair a new programmer with an old one. Add one test at the seam where fear accumulates.

With better understanding, smaller interventions become possible.

Musashi gives the severity. Ehn gives the participation. Naur gives the theory. Together they produce a humane pragmatism: cut waste, not people.

---

## 8. Documentation as Theory Trigger

The practical question remains: if theory cannot be fully written down, what should documentation do?

The answer is not “nothing.” That is a lazy misreading of Naur. Documentation matters. But its purpose changes. Documentation should not pretend to contain the whole theory. It should help the next person build an adequate theory.

This shift alters the content and style of good documentation.

Bad documentation says: here are all the parts.

Better documentation says: here is what this system is trying to do, how it maps onto the world, why its structure exists, which metaphors guide it, which alternatives were rejected, where the dangerous seams are, what kinds of modifications fit naturally, and what kinds of modifications would violate the theory.

Good documentation does not merely record decisions. It transmits judgment.

It might include metaphors, diagrams, examples, failure stories, modification walkthroughs, domain narratives, glossary entries, architectural scars, and warnings. It might show a real feature change from world demand to code modification. It might explain why a tempting shortcut is forbidden. It might identify the “shape” of good extensions.

The best documentation often has the tone of apprenticeship: “When you see this kind of problem, do not patch it here. This part looks like the right place, but it is not. The real model lives over there. We tried the obvious approach and it failed because…”

This is theory-building documentation.

It does not aim to be exhaustive. It aims to orient. It creates pathways of thought. It helps the next programmer ask better questions, make better guesses, and recognize meaningful similarities.

Ehn adds another layer: documentation may not be textual. A prototype, mockup, storyboard, test fixture, sandbox, executable example, or recorded walkthrough may teach more than a static document. If understanding is use, then the best documentation may be an environment in which the reader can act.

A test suite, for example, is not just a correctness mechanism. It is an executable theory of expected behavior. A good test names what matters. It teaches boundaries. It reveals what the system promises not to break. A bad test suite only freezes implementation trivia and makes change harder.

Likewise, a prototype can document possible use. A diagram can document relationships. A glossary can document conceptual boundaries. A commit history can document the evolution of judgment. A retrospective can document the theory of process.

The standard should be simple: does this artifact help someone join the living practice?

---

## 9. AI, Code Generation, and the Return of Theory

The rise of AI-assisted coding makes Naur more important, not less.

If code becomes cheaper to generate, the production view of programming becomes even more seductive. Organizations may assume that because text can be produced faster, programming has become easier. But if Naur is right, code generation accelerates only the production of one artifact. It does not automatically produce the theory required to judge, modify, integrate, and preserve the system.

AI can generate code without possessing responsibility for the theory of the program. It can mimic patterns, suggest implementations, explain fragments, and produce plausible structures. But the human team must still decide what matters, how the program maps to the world, what similarities are relevant, what tradeoffs are acceptable, and whether a generated solution belongs inside the system’s theory.

The danger is not that AI writes code. The danger is that teams accept code faster than they build understanding.

AI-generated software can decay instantly if no one owns the theory. A generated module may work locally while violating the architecture globally. It may pass tests while introducing conceptual duplication. It may satisfy the ticket while corrupting the model. The patch may be correct in behavior and wrong in theory.

This makes Naurian prompting essential. Before asking an AI system for program text, the team should force the theory into view: entities, operations, invariants, state transitions, assumptions, failure modes, change scenarios, and mapping between world and code. The point is not to bureaucratize prompting. The point is to prevent code generation from outrunning theory formation.

Ehn also matters here. AI tools should not only generate artifacts for users; they should support design language-games with users. They should help create mockups, scenarios, simulations, and prototypes through which users can act, judge, and reveal practical knowledge. The future of AI-assisted design should not be “requirements in, software out.” That is the old Cartesian fantasy in machine form.

The better model is participatory AI prototyping: users and designers shaping artifacts together, using AI to accelerate rehearsal without bypassing practice.

Musashi supplies the warning: do not become attached to the weapon. AI is a weapon. Sometimes it is the right weapon. Sometimes it produces flowers without fruit. Sometimes it helps the team cut directly to the problem. Sometimes it creates theatrical velocity while deepening confusion.

Use it. Do not worship it.

---

## 10. Toward a Humane Theory of Software Practice

Naur, Ehn, and Musashi give us a software ethic.

From Naur: preserve the theory.
From Ehn: stage shared practice.
From Musashi: cut waste and win.

Together they reject three dominant lies.

The first lie is that software is primarily code. It is not. Software is code animated by a human-held theory of its relation to the world.

The second lie is that users can fully describe what they need before they encounter the future tool. They cannot. Much of what matters emerges through situated use, mockup, rehearsal, and shared action.

The third lie is that the right method can save a team from judgment. It cannot. Methods are tools. Tools must be chosen, adapted, and abandoned by skilled practitioners.

A humane software practice begins by treating programmers, users, and designers as carriers of knowledge, not obstacles to process. It recognizes that skill cannot be fully extracted into documents. It designs handoffs as apprenticeships. It treats documentation as theory support. It builds prototypes not merely to validate requirements but to create shared experience. It uses methods lightly and deliberately. It keeps asking whether each artifact helps the team understand, coordinate, modify, and deliver.

Its process discipline is severe but not theatrical. It does not add ceremony to look serious. It does not worship tools because they are fashionable. It does not mistake velocity for progress. It does not treat teammates as enemies. It does not sacrifice living understanding to administrative convenience.

The central practice is alignment around the problem.

This is what makes “There’s only us” more than a sentimental line. It is a technical principle. If programming depends on shared theory, then every social fracture is also an epistemic fracture. When developers distrust users, theory breaks. When managers distrust programmers, theory breaks. When documentation replaces conversation, theory thins. When method replaces judgment, theory freezes. When code is generated faster than it is understood, theory collapses.

The team’s task is to keep the theory alive long enough to deliver and adaptable enough to survive change.

This is not soft. It is harder than method compliance. It requires craft, memory, conversation, courage, and restraint. It asks the team to know when to document and when to pair, when to prototype and when to delete, when to use the tool and when to put it down, when to patch and when to rebuild, when to make a small intervention and when the structure itself must change.

In the end, the measure is not whether the team followed the school. The measure is whether the team defeated the problem without destroying its own capacity to continue.

The living program is not the one with the most documentation, the purest architecture, the newest toolchain, or the most elaborate process. The living program is the one whose people can still explain it, justify it, change it, teach it, and use it to meet the world.

That is theory.
That is practice.
That is victory.
