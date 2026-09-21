# -*- coding: utf-8 -*-
"""
Dataset for the 99 Names of Allah (Asma ul Husna).

Each record:
    id            : 1-99
    arabic        : the name in Arabic script
    transliteration
    meaning       : short English meaning
    detail        : longer explanation
    quran         : a Qur'anic reference (or the source of the name)
    reflection    : a short note on applying / remembering the name
"""

NAMES = [
    {
        "id": 1, "arabic": "الرَّحْمَٰن", "transliteration": "Ar-Rahman",
        "meaning": "The Most Compassionate",
        "detail": "The One whose mercy is vast, immediate and all-embracing. Ar-Rahman describes a mercy that reaches every creature in this world without exception, believer and disbeliever alike, in the air they breathe and the sustenance they receive.",
        "quran": "Surah Ar-Rahman 55:1 — 'The Most Compassionate.'",
        "reflection": "Every breath you take is already an act of His mercy before you ask for anything."
    },
    {
        "id": 2, "arabic": "الرَّحِيم", "transliteration": "Ar-Rahim",
        "meaning": "The Most Merciful",
        "detail": "The One who continually pours out mercy. Where Ar-Rahman is mercy as an all-encompassing attribute, Ar-Rahim is mercy in action — specifically and eternally directed toward the believers, in this life and the next.",
        "quran": "Surah Al-Fatihah 1:3 — 'The Most Compassionate, the Most Merciful.'",
        "reflection": "Mercy is not earned by perfection; it is given to those who keep turning back."
    },
    {
        "id": 3, "arabic": "الْمَلِك", "transliteration": "Al-Malik",
        "meaning": "The Sovereign, The King",
        "detail": "The absolute King who owns all dominion and needs nothing from His kingdom. Every other authority is borrowed, temporary and answerable; His alone is intrinsic and unending.",
        "quran": "Surah Al-Hashr 59:23 — 'He is Allah, other than whom there is no deity, the Sovereign.'",
        "reflection": "Serving the true King frees you from serving a hundred smaller ones."
    },
    {
        "id": 4, "arabic": "الْقُدُّوس", "transliteration": "Al-Quddus",
        "meaning": "The Most Holy, Free of All Fault",
        "detail": "The One utterly pure and beyond every defect, deficiency or imperfection the mind could imagine. Nothing of creation's weakness attaches to Him.",
        "quran": "Surah Al-Hashr 59:23",
        "reflection": "Purifying the heart is how a servant draws near to the Pure."
    },
    {
        "id": 5, "arabic": "السَّلَام", "transliteration": "As-Salam",
        "meaning": "The Source of Peace",
        "detail": "The One who is Himself free from all flaw and who is the origin of every safety and peace His creation enjoys. Peace of heart is sought from Him alone.",
        "quran": "Surah Al-Hashr 59:23",
        "reflection": "The greeting of peace between people is borrowed from one of His own names."
    },
    {
        "id": 6, "arabic": "الْمُؤْمِن", "transliteration": "Al-Mu'min",
        "meaning": "The Giver of Faith and Security",
        "detail": "The One who grants security to His servants and confirms the truth of His messengers. He places faith in hearts and calms fear with certainty.",
        "quran": "Surah Al-Hashr 59:23",
        "reflection": "Turn to Him for safety when your own precautions run out."
    },
    {
        "id": 7, "arabic": "الْمُهَيْمِن", "transliteration": "Al-Muhaymin",
        "meaning": "The Guardian, The Overseer",
        "detail": "The One who watches over all things, preserves them, and has complete authority over their affairs. Nothing escapes His supervision for even a moment.",
        "quran": "Surah Al-Hashr 59:23",
        "reflection": "You are never unobserved — and never unprotected."
    },
    {
        "id": 8, "arabic": "الْعَزِيز", "transliteration": "Al-Aziz",
        "meaning": "The Almighty, The Invincible",
        "detail": "The One of complete might who can never be overcome, and whose honour no one can diminish. All true honour comes only from Him.",
        "quran": "Surah Al-Hashr 59:23",
        "reflection": "Seek dignity from the Almighty, not from the approval of people."
    },
    {
        "id": 9, "arabic": "الْجَبَّار", "transliteration": "Al-Jabbar",
        "meaning": "The Compeller, The Restorer",
        "detail": "The One whose will prevails over all, and who mends what is broken. The root jabr carries both compulsion and the setting of a fracture back into place.",
        "quran": "Surah Al-Hashr 59:23",
        "reflection": "He is the one who repairs hearts that nothing else could mend."
    },
    {
        "id": 10, "arabic": "الْمُتَكَبِّر", "transliteration": "Al-Mutakabbir",
        "meaning": "The Supreme in Greatness",
        "detail": "The One who is rightfully and uniquely great. Greatness is His alone; in a creature the same quality becomes arrogance, which He dislikes.",
        "quran": "Surah Al-Hashr 59:23",
        "reflection": "Humility is the only honest posture before true greatness."
    },
    {
        "id": 11, "arabic": "الْخَالِق", "transliteration": "Al-Khaliq",
        "meaning": "The Creator",
        "detail": "The One who brings all things into existence from nothing, determining their measure and destiny before they appear.",
        "quran": "Surah Al-Hashr 59:24",
        "reflection": "Nothing around you made itself; every detail was chosen."
    },
    {
        "id": 12, "arabic": "الْبَارِئ", "transliteration": "Al-Bari'",
        "meaning": "The Originator, The Maker",
        "detail": "The One who gives creation its distinct form and order, flawlessly and without any prior model to copy.",
        "quran": "Surah Al-Hashr 59:24",
        "reflection": "Every living thing is an original, never a duplicate."
    },
    {
        "id": 13, "arabic": "الْمُصَوِّر", "transliteration": "Al-Musawwir",
        "meaning": "The Fashioner of Forms",
        "detail": "The One who shapes each creature with a particular appearance, giving every face, voice and fingerprint its own signature.",
        "quran": "Surah Al-Hashr 59:24",
        "reflection": "Your form was designed, not accidental — do not despise it."
    },
    {
        "id": 14, "arabic": "الْغَفَّار", "transliteration": "Al-Ghaffar",
        "meaning": "The Ever-Forgiving",
        "detail": "The One who forgives repeatedly and conceals faults. The intensive form means forgiveness is not a single event but a constant, renewing quality.",
        "quran": "Surah Nuh 71:10 — 'Ask forgiveness of your Lord. Indeed, He is ever a Perpetual Forgiver.'",
        "reflection": "However many times you return, He has not tired of forgiving."
    },
    {
        "id": 15, "arabic": "الْقَهَّار", "transliteration": "Al-Qahhar",
        "meaning": "The All-Subduer",
        "detail": "The One whose power dominates everything; all creation is subdued beneath His will and no force can resist His decree.",
        "quran": "Surah Ar-Ra'd 13:16",
        "reflection": "What overwhelms you is itself subdued by Him."
    },
    {
        "id": 16, "arabic": "الْوَهَّاب", "transliteration": "Al-Wahhab",
        "meaning": "The Supreme Bestower",
        "detail": "The One who gives freely and continuously, expecting nothing in return and without being asked. His gifts are not payment but pure generosity.",
        "quran": "Surah Aal-Imran 3:8 — 'Indeed, You are the Bestower.'",
        "reflection": "Most of what you have, you never requested."
    },
    {
        "id": 17, "arabic": "الرَّزَّاق", "transliteration": "Ar-Razzaq",
        "meaning": "The Provider, The Sustainer",
        "detail": "The One who provides all sustenance — food, knowledge, companionship, opportunity — to every creature, arranging means they could never arrange themselves.",
        "quran": "Surah Adh-Dhariyat 51:58 — 'Indeed, it is Allah who is the Provider.'",
        "reflection": "Work for your provision, but know who actually sends it."
    },
    {
        "id": 18, "arabic": "الْفَتَّاح", "transliteration": "Al-Fattah",
        "meaning": "The Opener, The Reliever",
        "detail": "The One who opens what is closed — locked doors, closed hearts, blocked paths — and who judges between people with truth.",
        "quran": "Surah Saba 34:26",
        "reflection": "When every door seems shut, ask the One who holds the keys."
    },
    {
        "id": 19, "arabic": "الْعَلِيم", "transliteration": "Al-Alim",
        "meaning": "The All-Knowing",
        "detail": "The One whose knowledge is complete and without limit — of the past, the present, the future, the outward and the hidden thought no one else will ever hear.",
        "quran": "Surah Al-Baqarah 2:29",
        "reflection": "You do not have to explain yourself to the One who already knows."
    },
    {
        "id": 20, "arabic": "الْقَابِض", "transliteration": "Al-Qabid",
        "meaning": "The Withholder, The Constrictor",
        "detail": "The One who withholds and restricts provision, life or ease according to perfect wisdom. What He withholds is as purposeful as what He gives.",
        "quran": "Surah Al-Baqarah 2:245",
        "reflection": "A door held shut may be protection, not punishment."
    },
    {
        "id": 21, "arabic": "الْبَاسِط", "transliteration": "Al-Basit",
        "meaning": "The Extender, The Expander",
        "detail": "The One who expands provision, relief and the capacity of the heart. He widens what was narrow, at the moment He chooses.",
        "quran": "Surah Al-Baqarah 2:245",
        "reflection": "Constriction and expansion both come from the same hand."
    },
    {
        "id": 22, "arabic": "الْخَافِض", "transliteration": "Al-Khafid",
        "meaning": "The Abaser",
        "detail": "The One who lowers the arrogant and the tyrannical, bringing down whoever raises themselves unjustly above others.",
        "quran": "From the narration of the names (Jami' at-Tirmidhi)",
        "reflection": "No power stays high against His will."
    },
    {
        "id": 23, "arabic": "الرَّافِع", "transliteration": "Ar-Rafi'",
        "meaning": "The Exalter, The Elevator",
        "detail": "The One who raises in rank whom He wills — through faith, knowledge and sincerity rather than wealth or lineage.",
        "quran": "Surah Al-Mujadila 58:11",
        "reflection": "Real elevation is in status with Him, not status with people."
    },
    {
        "id": 24, "arabic": "الْمُعِز", "transliteration": "Al-Mu'izz",
        "meaning": "The Bestower of Honour",
        "detail": "The One who grants honour and strength to whom He wills. Honour given by Him cannot be taken by anyone.",
        "quran": "Surah Aal-Imran 3:26",
        "reflection": "Chase His pleasure and dignity follows on its own."
    },
    {
        "id": 25, "arabic": "الْمُذِل", "transliteration": "Al-Mudhill",
        "meaning": "The Humiliator",
        "detail": "The One who brings low whoever deserves it, stripping away false grandeur so the truth of a person becomes visible.",
        "quran": "Surah Aal-Imran 3:26",
        "reflection": "Never build your worth on something He can remove in a day."
    },
    {
        "id": 26, "arabic": "السَّمِيع", "transliteration": "As-Sami'",
        "meaning": "The All-Hearing",
        "detail": "The One who hears every sound — spoken and unspoken, in every language, all at once — including the prayer whispered in an empty room.",
        "quran": "Surah Ash-Shura 42:11",
        "reflection": "The quietest du'a is heard as clearly as the loudest."
    },
    {
        "id": 27, "arabic": "الْبَصِير", "transliteration": "Al-Basir",
        "meaning": "The All-Seeing",
        "detail": "The One who sees all things, however small or hidden, and who sees intentions as clearly as actions.",
        "quran": "Surah Al-Isra 17:1",
        "reflection": "Your unseen effort is not unseen."
    },
    {
        "id": 28, "arabic": "الْحَكَم", "transliteration": "Al-Hakam",
        "meaning": "The Impartial Judge",
        "detail": "The One who judges between His creation with absolute justice, whose verdict no one can appeal, delay or overturn.",
        "quran": "Surah Al-An'am 6:114",
        "reflection": "Every injustice has a court date you will not have to arrange."
    },
    {
        "id": 29, "arabic": "الْعَدْل", "transliteration": "Al-'Adl",
        "meaning": "The Utterly Just",
        "detail": "The One who is justice itself. He wrongs no one by even the weight of an atom, and gives each soul exactly what it is due.",
        "quran": "Surah An-Nisa 4:40",
        "reflection": "Be fair even when it costs you; you are imitating His attribute."
    },
    {
        "id": 30, "arabic": "اللَّطِيف", "transliteration": "Al-Latif",
        "meaning": "The Subtle, The Most Gentle",
        "detail": "The One who is gentle and kind in ways too fine to notice, arranging good for His servants through channels they never see.",
        "quran": "Surah Al-An'am 6:103",
        "reflection": "Look back and you will find kindnesses you did not recognise at the time."
    },
    {
        "id": 31, "arabic": "الْخَبِير", "transliteration": "Al-Khabir",
        "meaning": "The All-Aware",
        "detail": "The One aware of the inner reality of everything — not just what happens, but why, and what lies beneath it.",
        "quran": "Surah Al-An'am 6:18",
        "reflection": "He knows the story behind your struggle, not only the surface."
    },
    {
        "id": 32, "arabic": "الْحَلِيم", "transliteration": "Al-Halim",
        "meaning": "The Most Forbearing",
        "detail": "The One who does not hasten to punish despite having full power to do so, giving time and space for people to return.",
        "quran": "Surah Al-Baqarah 2:235",
        "reflection": "The delay you were given was a mercy, not an oversight."
    },
    {
        "id": 33, "arabic": "الْعَظِيم", "transliteration": "Al-'Azim",
        "meaning": "The Magnificent, The Supreme",
        "detail": "The One whose greatness no mind can encompass. Every description falls short of the reality of His magnificence.",
        "quran": "Surah Al-Baqarah 2:255 (Ayat al-Kursi)",
        "reflection": "Your problem is small in front of Him — say so in your du'a."
    },
    {
        "id": 34, "arabic": "الْغَفُور", "transliteration": "Al-Ghafur",
        "meaning": "The Great Forgiver",
        "detail": "The One who forgives completely and covers sins so thoroughly that their traces and shame are erased.",
        "quran": "Surah Al-Baqarah 2:173",
        "reflection": "Despair of His forgiveness is itself the mistake."
    },
    {
        "id": 35, "arabic": "الشَّكُور", "transliteration": "Ash-Shakur",
        "meaning": "The Most Appreciative",
        "detail": "The One who rewards small deeds with vast returns, appreciating sincere effort far beyond what it objectively deserves.",
        "quran": "Surah Fatir 35:30",
        "reflection": "No act of goodness is too small to be noticed and repaid."
    },
    {
        "id": 36, "arabic": "الْعَلِي", "transliteration": "Al-'Ali",
        "meaning": "The Most High",
        "detail": "The One exalted above all creation in essence, power and rank. Nothing is above Him and nothing is comparable to Him.",
        "quran": "Surah Al-Baqarah 2:255",
        "reflection": "Raise your gaze to the Highest and lesser things shrink."
    },
    {
        "id": 37, "arabic": "الْكَبِير", "transliteration": "Al-Kabir",
        "meaning": "The Most Great",
        "detail": "The One greater than everything, before whom the entire universe is small. All grandeur besides His is relative and borrowed.",
        "quran": "Surah Al-Hajj 22:62",
        "reflection": "Saying 'Allahu Akbar' reorders what you thought was big."
    },
    {
        "id": 38, "arabic": "الْحَفِيظ", "transliteration": "Al-Hafiz",
        "meaning": "The Preserver, The Protector",
        "detail": "The One who preserves and guards all things — His revelation, His creation, and the records of every deed.",
        "quran": "Surah Hud 11:57",
        "reflection": "Guard what He entrusted to you and He will guard you."
    },
    {
        "id": 39, "arabic": "الْمُقِيت", "transliteration": "Al-Muqit",
        "meaning": "The Sustainer, The Nourisher",
        "detail": "The One who supplies every creature with exactly the nourishment it needs and has full power over its sustenance.",
        "quran": "Surah An-Nisa 4:85",
        "reflection": "Your share will reach you; it cannot be eaten by someone else."
    },
    {
        "id": 40, "arabic": "الْحَسِيب", "transliteration": "Al-Hasib",
        "meaning": "The Reckoner, The Sufficient",
        "detail": "The One who takes account of every deed precisely, and who is Himself sufficient for whoever relies on Him.",
        "quran": "Surah An-Nisa 4:86",
        "reflection": "'Hasbunallah' — He alone is enough for us."
    },
    {
        "id": 41, "arabic": "الْجَلِيل", "transliteration": "Al-Jalil",
        "meaning": "The Majestic",
        "detail": "The One of true majesty and sublime attributes, whose glory inspires awe in every heart that perceives it.",
        "quran": "From the narration of the names (Jami' at-Tirmidhi)",
        "reflection": "Awe and love for Him are meant to grow together."
    },
    {
        "id": 42, "arabic": "الْكَرِيم", "transliteration": "Al-Karim",
        "meaning": "The Most Generous",
        "detail": "The One who gives without being asked, forgives when able to punish, and honours His servants beyond their deserving.",
        "quran": "Surah Al-Infitar 82:6",
        "reflection": "Ask generously; you are asking the Most Generous."
    },
    {
        "id": 43, "arabic": "الرَّقِيب", "transliteration": "Ar-Raqib",
        "meaning": "The Ever-Watchful",
        "detail": "The One who watches over everything constantly, never distracted and never asleep, observing every soul at every instant.",
        "quran": "Surah An-Nisa 4:1",
        "reflection": "Integrity in private is the proof that you believe this name."
    },
    {
        "id": 44, "arabic": "الْمُجِيب", "transliteration": "Al-Mujib",
        "meaning": "The Responsive One",
        "detail": "The One who answers the caller — sometimes with what was asked, sometimes with something better, sometimes by removing a harm you never saw.",
        "quran": "Surah Hud 11:61 — 'Indeed, my Lord is near and responsive.'",
        "reflection": "No du'a is wasted; only the form of the answer varies."
    },
    {
        "id": 45, "arabic": "الْوَاسِع", "transliteration": "Al-Wasi'",
        "meaning": "The All-Encompassing",
        "detail": "The One whose knowledge, mercy and provision are boundless. Giving to one servant never reduces what is available to another.",
        "quran": "Surah Al-Baqarah 2:115",
        "reflection": "There is no scarcity in His treasury to be jealous over."
    },
    {
        "id": 46, "arabic": "الْحَكِيم", "transliteration": "Al-Hakim",
        "meaning": "The All-Wise",
        "detail": "The One who places everything in its right place at its right time. Nothing in His decree is arbitrary, even when the wisdom is hidden from us.",
        "quran": "Surah Al-Baqarah 2:32",
        "reflection": "What you would not have chosen may be exactly what was wise."
    },
    {
        "id": 47, "arabic": "الْوَدُود", "transliteration": "Al-Wadud",
        "meaning": "The Most Loving",
        "detail": "The One who loves His righteous servants and is beloved to them. His love is active, expressed in care rather than mere sentiment.",
        "quran": "Surah Hud 11:90 — 'Indeed, my Lord is Merciful and Loving.'",
        "reflection": "You are not merely tolerated by your Lord; you can be loved by Him."
    },
    {
        "id": 48, "arabic": "الْمَجِيد", "transliteration": "Al-Majid",
        "meaning": "The Glorious, The Most Honourable",
        "detail": "The One who combines perfect glory with perfect generosity — majestic in His essence and noble in His dealings with creation.",
        "quran": "Surah Hud 11:73",
        "reflection": "Glory and kindness are not opposites in Him."
    },
    {
        "id": 49, "arabic": "الْبَاعِث", "transliteration": "Al-Ba'ith",
        "meaning": "The Resurrector",
        "detail": "The One who raises the dead to life for the Day of Judgement, and who sends messengers to awaken hearts that had died to the truth.",
        "quran": "Surah Al-Hajj 22:7",
        "reflection": "A heart, like a body, can be brought back to life by Him."
    },
    {
        "id": 50, "arabic": "الشَّهِيد", "transliteration": "Ash-Shahid",
        "meaning": "The All-Observing Witness",
        "detail": "The One present to everything and witness over everything. Nothing occurs outside His direct witnessing.",
        "quran": "Surah An-Nisa 4:79",
        "reflection": "When no one else saw what happened to you, He did."
    },
    {
        "id": 51, "arabic": "الْحَق", "transliteration": "Al-Haqq",
        "meaning": "The Absolute Truth",
        "detail": "The One whose existence, words and promises are absolutely real. Everything else is contingent; He alone is the reality behind all realities.",
        "quran": "Surah Al-Hajj 22:6",
        "reflection": "Anchor yourself to what is real, not to what merely appears."
    },
    {
        "id": 52, "arabic": "الْوَكِيل", "transliteration": "Al-Wakil",
        "meaning": "The Trustee, The Disposer of Affairs",
        "detail": "The One to whom affairs can be entrusted completely. He manages what you cannot, once you have done what you can.",
        "quran": "Surah Aal-Imran 3:173 — 'Sufficient for us is Allah, and He is the best Disposer of affairs.'",
        "reflection": "Tie your camel, then hand the rope to Him."
    },
    {
        "id": 53, "arabic": "الْقَوِي", "transliteration": "Al-Qawiyy",
        "meaning": "The All-Strong",
        "detail": "The One of complete strength that never weakens or depletes, however much of it is exercised.",
        "quran": "Surah Adh-Dhariyat 51:58",
        "reflection": "Borrow strength from the Strong when yours runs out."
    },
    {
        "id": 54, "arabic": "الْمَتِين", "transliteration": "Al-Matin",
        "meaning": "The Firm, The Steadfast",
        "detail": "The One whose power is firm and unshakeable, requiring no support, no rest and no recovery.",
        "quran": "Surah Adh-Dhariyat 51:58",
        "reflection": "Stand on ground that does not move."
    },
    {
        "id": 55, "arabic": "الْوَلِي", "transliteration": "Al-Waliyy",
        "meaning": "The Protecting Friend",
        "detail": "The One who is the ally and guardian of the believers, taking them out of darkness into light and defending them when they have no other defender.",
        "quran": "Surah Al-Baqarah 2:257",
        "reflection": "Having Him as your ally outweighs every other alliance."
    },
    {
        "id": 56, "arabic": "الْحَمِيد", "transliteration": "Al-Hamid",
        "meaning": "The Praiseworthy",
        "detail": "The One deserving of all praise in every circumstance, whether or not anyone praises Him. Praise is due to Him for His essence, not only His gifts.",
        "quran": "Surah Ibrahim 14:8",
        "reflection": "'Alhamdulillah' in hardship is the harder and greater praise."
    },
    {
        "id": 57, "arabic": "الْمُحْصِي", "transliteration": "Al-Muhsi",
        "meaning": "The All-Enumerating",
        "detail": "The One who counts and records everything precisely — every deed, every word, every grain and every breath.",
        "quran": "Surah Maryam 19:94",
        "reflection": "Nothing good you did has been lost from the record."
    },
    {
        "id": 58, "arabic": "الْمُبْدِئ", "transliteration": "Al-Mubdi'",
        "meaning": "The Originator of Creation",
        "detail": "The One who begins creation from nothing, with no prior example and no assistance.",
        "quran": "Surah Al-Buruj 85:13",
        "reflection": "The One who started you from nothing can restart anything for you."
    },
    {
        "id": 59, "arabic": "الْمُعِيد", "transliteration": "Al-Mu'id",
        "meaning": "The Restorer, The Reinstater",
        "detail": "The One who brings creation back after its end, and who restores what was lost to its rightful place.",
        "quran": "Surah Al-Buruj 85:13",
        "reflection": "Endings in His hands are often only intervals."
    },
    {
        "id": 60, "arabic": "الْمُحْيِي", "transliteration": "Al-Muhyi",
        "meaning": "The Giver of Life",
        "detail": "The One who gives life to bodies, to barren earth after rain, and to hearts after heedlessness.",
        "quran": "Surah Ar-Rum 30:50",
        "reflection": "The rain that revives dead land is a lesson about your heart."
    },
    {
        "id": 61, "arabic": "الْمُمِيت", "transliteration": "Al-Mumit",
        "meaning": "The Bringer of Death",
        "detail": "The One who ordains death at its appointed time. Death is not a failure of the system but a decreed part of it.",
        "quran": "Surah Aal-Imran 3:156",
        "reflection": "Remembering death makes trivial things fall into proportion."
    },
    {
        "id": 62, "arabic": "الْحَي", "transliteration": "Al-Hayy",
        "meaning": "The Ever-Living",
        "detail": "The One whose life is perfect and eternal, with no beginning, no end, and no dependence on anything else for its continuation.",
        "quran": "Surah Al-Baqarah 2:255",
        "reflection": "'Ya Hayyu ya Qayyum' — a du'a for when you feel depleted."
    },
    {
        "id": 63, "arabic": "الْقَيُّوم", "transliteration": "Al-Qayyum",
        "meaning": "The Self-Subsisting Sustainer",
        "detail": "The One who exists by Himself and by whom everything else is maintained. If His sustaining stopped for an instant, all existence would collapse.",
        "quran": "Surah Al-Baqarah 2:255",
        "reflection": "You are being held up right now, continuously."
    },
    {
        "id": 64, "arabic": "الْوَاجِد", "transliteration": "Al-Wajid",
        "meaning": "The Perceiver, The Finder",
        "detail": "The One who lacks nothing and finds whatever He wills whenever He wills. Nothing is missing from Him or hidden to Him.",
        "quran": "From the narration of the names (Jami' at-Tirmidhi)",
        "reflection": "He can find for you what you have no way of finding."
    },
    {
        "id": 65, "arabic": "الْمَاجِد", "transliteration": "Al-Majid",
        "meaning": "The Noble, The Illustrious",
        "detail": "The One of abundant nobility and honour, whose generosity toward His creation matches the glory of His essence.",
        "quran": "From the narration of the names (Jami' at-Tirmidhi)",
        "reflection": "Nobility of character is a reflection of His name."
    },
    {
        "id": 66, "arabic": "الْوَاحِد", "transliteration": "Al-Wahid",
        "meaning": "The One",
        "detail": "The One and only, unique in His essence, attributes and actions, with no partner, equal or rival.",
        "quran": "Surah Ar-Ra'd 13:16",
        "reflection": "One Lord means one direction for the heart."
    },
    {
        "id": 67, "arabic": "الْأَحَد", "transliteration": "Al-Ahad",
        "meaning": "The Unique, The Indivisible",
        "detail": "The One who is indivisible and absolutely singular — not one of a series, and not composed of parts.",
        "quran": "Surah Al-Ikhlas 112:1 — 'Say: He is Allah, the One.'",
        "reflection": "Tawhid begins with this name and ends with it."
    },
    {
        "id": 68, "arabic": "الصَّمَد", "transliteration": "As-Samad",
        "meaning": "The Eternal Refuge",
        "detail": "The One upon whom all creation depends while He depends on none. Every need eventually terminates at His door.",
        "quran": "Surah Al-Ikhlas 112:2",
        "reflection": "Every other refuge is itself in need of refuge."
    },
    {
        "id": 69, "arabic": "الْقَادِر", "transliteration": "Al-Qadir",
        "meaning": "The All-Capable",
        "detail": "The One able to do all things — able to give, to withhold, and to change any situation at once.",
        "quran": "Surah Al-An'am 6:65",
        "reflection": "Nothing you are asking for is difficult for Him."
    },
    {
        "id": 70, "arabic": "الْمُقْتَدِر", "transliteration": "Al-Muqtadir",
        "meaning": "The Omnipotent, The Determiner",
        "detail": "The One of prevailing, decisive power, who carries out what He determines without obstacle or delay.",
        "quran": "Surah Al-Qamar 54:42",
        "reflection": "His decree arrives on time, never early and never late."
    },
    {
        "id": 71, "arabic": "الْمُقَدِّم", "transliteration": "Al-Muqaddim",
        "meaning": "The Expediter, The Promoter",
        "detail": "The One who brings forward whatever and whoever He wills, advancing people and events according to His wisdom.",
        "quran": "From the narration of the names (Jami' at-Tirmidhi)",
        "reflection": "Someone else moving ahead of you was also His decision."
    },
    {
        "id": 72, "arabic": "الْمُؤَخِّر", "transliteration": "Al-Mu'akhkhir",
        "meaning": "The Delayer",
        "detail": "The One who delays what He wills to its appointed time. Delay in His hand is placement, not neglect.",
        "quran": "Surah Ibrahim 14:42",
        "reflection": "What is late for you may be exactly on time for Him."
    },
    {
        "id": 73, "arabic": "الْأَوَّل", "transliteration": "Al-Awwal",
        "meaning": "The First, The Beginningless",
        "detail": "The One who was before everything, with no beginning to His existence and nothing preceding Him.",
        "quran": "Surah Al-Hadid 57:3",
        "reflection": "He was there before your story started."
    },
    {
        "id": 74, "arabic": "الْآخِر", "transliteration": "Al-Akhir",
        "meaning": "The Last, The Endless",
        "detail": "The One who remains after everything ends, with no conclusion to His existence.",
        "quran": "Surah Al-Hadid 57:3",
        "reflection": "He will still be there after everything you fear has passed."
    },
    {
        "id": 75, "arabic": "الظَّاهِر", "transliteration": "Az-Zahir",
        "meaning": "The Manifest",
        "detail": "The One evident above all through the signs of His creation; His existence is clearer than anything else if you look honestly.",
        "quran": "Surah Al-Hadid 57:3",
        "reflection": "The evidence is not scarce; the attention is."
    },
    {
        "id": 76, "arabic": "الْبَاطِن", "transliteration": "Al-Batin",
        "meaning": "The Hidden, The Knower of the Unseen",
        "detail": "The One whose essence is beyond perception, nearer to His servants than they imagine while remaining unseen.",
        "quran": "Surah Al-Hadid 57:3",
        "reflection": "Not visible does not mean not present."
    },
    {
        "id": 77, "arabic": "الْوَالِي", "transliteration": "Al-Wali",
        "meaning": "The Governor, The Patron",
        "detail": "The One who governs and manages all creation, directing every affair with full authority and care.",
        "quran": "Surah Ar-Ra'd 13:11",
        "reflection": "The universe is governed, not drifting."
    },
    {
        "id": 78, "arabic": "الْمُتَعَالِي", "transliteration": "Al-Muta'ali",
        "meaning": "The Most Exalted",
        "detail": "The One far above every limitation, false attribution or inadequate description that people assign to Him.",
        "quran": "Surah Ar-Ra'd 13:9",
        "reflection": "Speak about Him with care; He is above your best words."
    },
    {
        "id": 79, "arabic": "الْبَر", "transliteration": "Al-Barr",
        "meaning": "The Source of All Goodness",
        "detail": "The One abundantly kind and good to His creation, whose goodness reaches even those who forget Him.",
        "quran": "Surah At-Tur 52:28",
        "reflection": "Goodness you receive from others originates with Him."
    },
    {
        "id": 80, "arabic": "التَّوَّاب", "transliteration": "At-Tawwab",
        "meaning": "The Ever-Accepting of Repentance",
        "detail": "The One who turns repeatedly toward His servants, inspiring them to repent and then accepting that repentance when they do.",
        "quran": "Surah Al-Baqarah 2:37",
        "reflection": "He turned to you first — that is why you wanted to return."
    },
    {
        "id": 81, "arabic": "الْمُنْتَقِم", "transliteration": "Al-Muntaqim",
        "meaning": "The Avenger",
        "detail": "The One who justly requites the oppressor after ample opportunity for repentance has been given and refused.",
        "quran": "Surah As-Sajdah 32:22",
        "reflection": "Leave the account of your oppressor with Him."
    },
    {
        "id": 82, "arabic": "الْعَفُو", "transliteration": "Al-'Afuww",
        "meaning": "The Pardoner, The Effacer of Sins",
        "detail": "The One who not only forgives but erases the sin entirely, so that no trace of it remains to be mentioned.",
        "quran": "Surah An-Nisa 4:99",
        "reflection": "'Allahumma innaka 'Afuwwun tuhibbul-'afwa fa'fu 'anni.'"
    },
    {
        "id": 83, "arabic": "الرَّءُوف", "transliteration": "Ar-Ra'uf",
        "meaning": "The Most Kind, The Compassionate",
        "detail": "The One of the most tender compassion, who does not burden a soul beyond its capacity and lightens what He can.",
        "quran": "Surah Al-Baqarah 2:143",
        "reflection": "His compassion is gentler than you expect of yourself."
    },
    {
        "id": 84, "arabic": "مَالِكُ الْمُلْك", "transliteration": "Malik-ul-Mulk",
        "meaning": "Owner of All Sovereignty",
        "detail": "The Owner of all dominion, who gives authority to whom He wills and removes it from whom He wills.",
        "quran": "Surah Aal-Imran 3:26",
        "reflection": "Every throne on earth is on loan."
    },
    {
        "id": 85, "arabic": "ذُو الْجَلَالِ وَالْإِكْرَام", "transliteration": "Dhul-Jalali wal-Ikram",
        "meaning": "Lord of Majesty and Generosity",
        "detail": "The One who possesses both overwhelming majesty and overflowing honour and generosity toward His servants.",
        "quran": "Surah Ar-Rahman 55:78",
        "reflection": "Fear His majesty and hope in His generosity, together."
    },
    {
        "id": 86, "arabic": "الْمُقْسِط", "transliteration": "Al-Muqsit",
        "meaning": "The Equitable, The Just",
        "detail": "The One who establishes equity, restores the rights of the wronged, and is pleased with those who deal fairly.",
        "quran": "Surah Aal-Imran 3:18",
        "reflection": "Fairness in small matters is worship."
    },
    {
        "id": 87, "arabic": "الْجَامِع", "transliteration": "Al-Jami'",
        "meaning": "The Gatherer, The Uniter",
        "detail": "The One who gathers all creation on the Day of Judgement, and who unites hearts, families and scattered affairs.",
        "quran": "Surah Aal-Imran 3:9",
        "reflection": "He can bring back together what has been scattered."
    },
    {
        "id": 88, "arabic": "الْغَنِي", "transliteration": "Al-Ghaniyy",
        "meaning": "The Self-Sufficient, The Rich",
        "detail": "The One utterly free of need. Our worship benefits us, never Him; He is not enriched by our obedience.",
        "quran": "Surah Muhammad 47:38",
        "reflection": "True wealth is contentment of heart, not accumulation."
    },
    {
        "id": 89, "arabic": "الْمُغْنِي", "transliteration": "Al-Mughni",
        "meaning": "The Enricher",
        "detail": "The One who enriches whom He wills, with wealth, with knowledge, or with a contentment more valuable than either.",
        "quran": "Surah An-Najm 53:48",
        "reflection": "Ask Him for sufficiency, not just for more."
    },
    {
        "id": 90, "arabic": "الْمَانِع", "transliteration": "Al-Mani'",
        "meaning": "The Preventer, The Withholder",
        "detail": "The One who withholds and prevents what would cause harm, protecting His servants from things they were eager to have.",
        "quran": "From the narration of the names (Jami' at-Tirmidhi)",
        "reflection": "Some of your unanswered du'as were answered by being refused."
    },
    {
        "id": 91, "arabic": "الضَّار", "transliteration": "Ad-Darr",
        "meaning": "The Creator of Harm",
        "detail": "The One in whose power alone harm occurs, always by wisdom and never by injustice. Nothing hurts you except by His permission.",
        "quran": "Surah Al-An'am 6:17",
        "reflection": "Fear the One who permits harm, not the thing itself."
    },
    {
        "id": 92, "arabic": "النَّافِع", "transliteration": "An-Nafi'",
        "meaning": "The Bestower of Benefit",
        "detail": "The One who is the source of all benefit. No person or means can help you unless He makes it beneficial.",
        "quran": "Surah Al-An'am 6:17",
        "reflection": "Ask Him for benefit in the means, not only the means."
    },
    {
        "id": 93, "arabic": "النُّور", "transliteration": "An-Nur",
        "meaning": "The Light",
        "detail": "The Light of the heavens and the earth, who illuminates existence and guides hearts out of confusion into clarity.",
        "quran": "Surah An-Nur 24:35",
        "reflection": "Knowledge is light; ask Him to place it in your heart."
    },
    {
        "id": 94, "arabic": "الْهَادِي", "transliteration": "Al-Hadi",
        "meaning": "The Guide",
        "detail": "The One who guides to the truth. No teacher, book or argument can guide a heart unless He opens it.",
        "quran": "Surah Al-Hajj 22:54",
        "reflection": "You ask for guidance seventeen times a day in Al-Fatihah."
    },
    {
        "id": 95, "arabic": "الْبَدِيع", "transliteration": "Al-Badi'",
        "meaning": "The Incomparable Originator",
        "detail": "The One who originates without precedent — creating forms and orders that no eye had seen and no mind had conceived.",
        "quran": "Surah Al-Baqarah 2:117",
        "reflection": "Originality in creation points back to the Originator."
    },
    {
        "id": 96, "arabic": "الْبَاقِي", "transliteration": "Al-Baqi",
        "meaning": "The Everlasting",
        "detail": "The One who remains when everything else perishes. Permanence belongs to Him alone.",
        "quran": "Surah Ar-Rahman 55:26-27",
        "reflection": "Invest in what lasts, for the rest is already expiring."
    },
    {
        "id": 97, "arabic": "الْوَارِث", "transliteration": "Al-Warith",
        "meaning": "The Inheritor of All",
        "detail": "The One to whom everything returns after its owners pass away. He is the final inheritor of the heavens and the earth.",
        "quran": "Surah Al-Hijr 15:23",
        "reflection": "Nothing you own is going with you."
    },
    {
        "id": 98, "arabic": "الرَّشِيد", "transliteration": "Ar-Rashid",
        "meaning": "The Guide to the Right Path",
        "detail": "The One who directs His creation toward what is right and whose every decree is rightly guided and perfectly ordered.",
        "quran": "From the narration of the names (Jami' at-Tirmidhi)",
        "reflection": "His plan is more rightly guided than your preference."
    },
    {
        "id": 99, "arabic": "الصَّبُور", "transliteration": "As-Sabur",
        "meaning": "The Most Patient",
        "detail": "The One of infinite patience, who does not rush judgement despite full power, giving His servants time again and again.",
        "quran": "From the narration of the names (Jami' at-Tirmidhi)",
        "reflection": "His patience with you is the model for your patience with others."
    },
]


def get_all():
    """Light list for the grid — no long text."""
    return [
        {
            "id": n["id"],
            "arabic": n["arabic"],
            "transliteration": n["transliteration"],
            "meaning": n["meaning"],
        }
        for n in NAMES
    ]


def get_one(name_id):
    """Full record for a single name, or None."""
    for n in NAMES:
        if n["id"] == name_id:
            return n
    return None


def search(term):
    t = (term or "").strip().lower()
    if not t:
        return get_all()
    out = []
    for n in NAMES:
        if (t in n["transliteration"].lower()
                or t in n["meaning"].lower()
                or t in n["detail"].lower()
                or t in n["arabic"]
                or t == str(n["id"])):
            out.append({
                "id": n["id"],
                "arabic": n["arabic"],
                "transliteration": n["transliteration"],
                "meaning": n["meaning"],
            })
    return out
