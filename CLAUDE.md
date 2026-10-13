# Afspraken voor deze app

1. Eén `app.py` voor de interface; de logica staat in aparte, benoemde functies.
2. `requirements.txt` bevat enkel wat de app importeert, met vaste versienummers.
3. Een nieuw package toevoegen? Eerst vragen, met reden en alternatief. Niets installeren zonder akkoord.
4. Data staat in `data/`, geheimen in `.env`. Beide staan (samen met `__pycache__/` en `.venv/`) in `.gitignore`.
5. Elke werkende stap wordt gecommit met een duidelijke boodschap, nooit zonder dat de wijziging eerst getoond is.
6. Dit is cursuswerk zonder echte JIRA-taken. De org-policy eist toch een ticketreferentie in branchnaam en commits; in afspraak met de gebruiker gebruiken we daarvoor de placeholder `SYNTRA-0` (geen bestaand ticket).
