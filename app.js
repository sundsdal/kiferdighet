/* KI-ferdigheter.no – katalog med søk og taggfilter. Ingen avhengigheter. */
(() => {
  var sokEl = document.getElementById("sok");
  var taggEl = document.getElementById("tagger");
  var listeEl = document.getElementById("liste");
  var tomEl = document.getElementById("tom");
  var nullstillEl = document.getElementById("nullstill");

  var alle = [];
  var valgtTagg = null;

  function hentTagger() {
    var sett = new Set();
    alle.forEach((f) => {
      (f.tagger || []).forEach((t) => {
        sett.add(t);
      });
    });
    return Array.from(sett).sort((a, b) => a.localeCompare(b, "nb"));
  }

  function tegnKort(f) {
    var art = document.createElement("article");
    art.className = "kort";

    var tittel = document.createElement("p");
    tittel.className = "tittel";
    tittel.textContent = f.tittel || f.navn;
    art.appendChild(tittel);

    var beskrivelse = document.createElement("p");
    beskrivelse.textContent = f.beskrivelse || "";
    art.appendChild(beskrivelse);

    var taggRad = document.createElement("div");
    (f.tagger || []).forEach((t) => {
      var s = document.createElement("span");
      s.className = "tagg";
      s.textContent = t;
      taggRad.appendChild(s);
    });
    art.appendChild(taggRad);

    var lenker = document.createElement("div");
    lenker.className = "lenker";

    var les = document.createElement("a");
    les.href = f.sti;
    les.textContent = "Les SKILL.md";
    lenker.appendChild(les);

    var kopier = document.createElement("a");
    kopier.href = "#";
    kopier.textContent = "Kopier installasjon";
    kopier.addEventListener("click", (e) => {
      e.preventDefault();
      var kommando =
        "cp -R " +
        f.sti.replace("/SKILL.md", "") +
        " ~/.claude/skills/" +
        f.navn;
      kopierTekst(kommando, kopier);
    });
    lenker.appendChild(kopier);
    art.appendChild(lenker);

    return art;
  }

  function kopierTekst(tekst, el) {
    function tilbakemelding(ok) {
      if (!el) return;
      var opprinnelig = el.textContent;
      el.textContent = ok ? "Kopiert!" : "Kopiering feilet";
      setTimeout(() => {
        el.textContent = opprinnelig;
      }, 1500);
    }
    if (navigator.clipboard?.writeText) {
      navigator.clipboard.writeText(tekst).then(
        () => {
          tilbakemelding(true);
        },
        () => {
          tilbakemelding(false);
        },
      );
    } else {
      tilbakemelding(false);
    }
  }

  function matcher(f, q) {
    if (valgtTagg && (f.tagger || []).indexOf(valgtTagg) === -1) return false;
    if (!q) return true;
    var hay = (
      (f.tittel || "") +
      " " +
      (f.navn || "") +
      " " +
      (f.beskrivelse || "") +
      " " +
      (f.tagger || []).join(" ")
    ).toLowerCase();
    return q
      .toLowerCase()
      .split(/\s+/)
      .every((ord) => hay.indexOf(ord) !== -1);
  }

  function tegn() {
    var q = sokEl ? sokEl.value.trim() : "";
    listeEl.innerHTML = "";
    var viste = 0;
    alle.forEach((f) => {
      if (!matcher(f, q)) return;
      listeEl.appendChild(tegnKort(f));
      viste += 1;
    });
    tomEl.hidden = viste !== 0;

    // Taggknapper
    taggEl.innerHTML = "";
    hentTagger().forEach((t) => {
      var b = document.createElement("button");
      b.textContent = t;
      b.setAttribute("aria-pressed", valgtTagg === t ? "true" : "false");
      if (valgtTagg === t) b.classList.add("valgt");
      b.addEventListener("click", () => {
        valgtTagg = valgtTagg === t ? null : t;
        tegn();
      });
      taggEl.appendChild(b);
    });
  }

  // Faner for installer-guider
  document.querySelectorAll("[data-fane]").forEach((knapp) => {
    knapp.addEventListener("click", () => {
      document.querySelectorAll("[data-fane]").forEach((k) => {
        k.setAttribute("aria-selected", k === knapp ? "true" : "false");
      });
      var navn = knapp.getAttribute("data-fane");
      document.querySelectorAll("[data-panel]").forEach((p) => {
        p.hidden = p.getAttribute("data-panel") !== navn;
      });
    });
  });

  // Kopier-knapper
  document.querySelectorAll("[data-kopier]").forEach((knapp) => {
    knapp.addEventListener("click", () => {
      kopierTekst(knapp.getAttribute("data-kopier") || "", knapp);
    });
  });

  if (nullstillEl) {
    nullstillEl.addEventListener("click", () => {
      if (sokEl) sokEl.value = "";
      valgtTagg = null;
      tegn();
    });
  }
  if (sokEl) sokEl.addEventListener("input", tegn);

  fetch("skills.json")
    .then((r) => {
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.json();
    })
    .then((data) => {
      alle = data.ferdigheter || [];
      tegn();
    })
    .catch(() => {
      listeEl.innerHTML = "<p>Kunne ikke laste skills.json.</p>";
    });
})();
