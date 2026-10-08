// =============================================================================
// GARHWALI LANGUAGE PLAYGROUND — FRONTEND CLIENT JAVASCRIPT
// =============================================================================

document.addEventListener("DOMContentLoaded", () => {
  initTabs();
  initTranslator();
  initVoice();
  initDictionary();
  initConjugator();
  initNumbers();
  initFolklore();
  initReader();
});

// -----------------------------------------------------------------------------
// 1. Navigation Tabs
// -----------------------------------------------------------------------------
function initTabs() {
  const navBtns = document.querySelectorAll(".nav-btn");
  const tabContents = document.querySelectorAll(".tab-content");

  navBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      const targetId = btn.getAttribute("data-tab");
      navBtns.forEach((b) => b.classList.remove("active"));
      tabContents.forEach((t) => t.classList.remove("active"));

      btn.classList.add("active");
      const target = document.getElementById(targetId);
      if (target) {
        target.classList.add("active");
      }
    });
  });
}

// -----------------------------------------------------------------------------
// 2. Universal Translator
// -----------------------------------------------------------------------------
function initTranslator() {
  const transInput = document.getElementById("trans-input");
  const btnTranslate = document.getElementById("btn-translate");
  const btnClear = document.getElementById("btn-clear-trans");
  const outText = document.getElementById("trans-output-text");
  const outRoman = document.getElementById("trans-output-roman");
  const outMeta = document.getElementById("trans-output-meta");

  const selSource = document.getElementById("trans-source");
  const selDialect = document.getElementById("trans-dialect");
  const selMethod = document.getElementById("trans-method");

  async function performTranslation() {
    const text = transInput.value.trim();
    if (!text) return;

    outText.textContent = "Translating...";
    outRoman.textContent = "";
    outMeta.textContent = "";

    try {
      const res = await fetch("/api/translate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          text: text,
          source: selSource.value,
          dialect: selDialect.value,
          method: selMethod.value
        })
      });
      const data = await res.json();
      outText.textContent = data.translated_text || "—";
      outRoman.textContent = data.romanized ? `(${data.romanized})` : "";
      outMeta.textContent = `Source: ${data.source_lang.toUpperCase()} • Dialect: ${data.dialect} • Engine: ${data.method} (Confidence: ${(data.confidence * 100).toFixed(0)}%)`;
    } catch (err) {
      outText.textContent = "Translation failed. Check connection.";
      outMeta.textContent = String(err);
    }
  }

  btnTranslate.addEventListener("click", performTranslation);
  transInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) {
      performTranslation();
    }
  });

  btnClear.addEventListener("click", () => {
    transInput.value = "";
    outText.textContent = "Translation will appear here...";
    outRoman.textContent = "";
    outMeta.textContent = "";
  });

  document.querySelectorAll(".chip-btn").forEach((chip) => {
    chip.addEventListener("click", () => {
      transInput.value = chip.getAttribute("data-fill");
      performTranslation();
    });
  });
}

// -----------------------------------------------------------------------------
// 3. Voice & Audio
// -----------------------------------------------------------------------------
let currentAudio = null;

function initVoice() {
  const voiceInput = document.getElementById("voice-text-input");
  const btnSynthesize = document.getElementById("btn-voice-synthesize");
  const resultBox = document.getElementById("voice-result-box");
  const devText = document.getElementById("voice-dev-text");
  const romanText = document.getElementById("voice-roman-text");
  const btnPlay = document.getElementById("btn-play-audio");
  const audioStatus = document.getElementById("audio-status");
  const sylList = document.getElementById("voice-syllables-list");
  const ssmlCode = document.getElementById("voice-ssml-code");
  const selCat = document.getElementById("voice-category");
  const phrasesContainer = document.getElementById("phrases-container");

  let audioBase64 = null;

  async function performVoiceTranslation(textToSpeak) {
    const text = (textToSpeak || voiceInput.value).trim();
    if (!text) return;

    btnSynthesize.textContent = "Synthesizing...";
    btnSynthesize.disabled = true;

    try {
      const res = await fetch("/api/voice/translate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          text: text,
          generate_audio: true
        })
      });
      const data = await res.json();
      resultBox.style.display = "block";
      devText.textContent = data.translated_text;
      romanText.textContent = data.romanized;
      audioBase64 = data.audio_wav_base64;
      ssmlCode.textContent = data.ssml;

      // Render Syllables
      sylList.innerHTML = "";
      if (Array.isArray(data.syllables)) {
        data.syllables.forEach((s) => {
          const sp = document.createElement("span");
          sp.className = "syl-chip";
          sp.textContent = s;
          sylList.appendChild(sp);
        });
      }

      audioStatus.textContent = audioBase64 ? "Audio Ready" : "SSML Ready";
    } catch (err) {
      alert("Voice synthesis failed: " + err);
    } finally {
      btnSynthesize.textContent = "Synthesize Speech";
      btnSynthesize.disabled = false;
    }
  }

  btnSynthesize.addEventListener("click", () => performVoiceTranslation());

  btnPlay.addEventListener("click", () => {
    if (audioBase64) {
      if (currentAudio) currentAudio.pause();
      currentAudio = new Audio("data:audio/wav;base64," + audioBase64);
      audioStatus.textContent = "Playing...";
      currentAudio.play();
      currentAudio.onended = () => {
        audioStatus.textContent = "Playback Finished";
      };
    } else {
      // Fallback to pcm audio endpoint
      if (currentAudio) currentAudio.pause();
      currentAudio = new Audio("/api/voice/wav?duration=0.6&freq=440.0");
      currentAudio.play();
    }
  });

  async function loadPhrases(cat = "all") {
    try {
      const res = await fetch(`/api/voice/phrases?category=${encodeURIComponent(cat)}`);
      const data = await res.json();
      phrasesContainer.innerHTML = "";
      (data.phrases || []).forEach((p) => {
        const card = document.createElement("div");
        card.className = "phrase-card";
        card.innerHTML = `
          <div class="phrase-gbm">${p.garhwali}</div>
          <div class="phrase-en">${p.english} (${p.hindi})</div>
          <div class="phrase-cat">${p.category}</div>
        `;
        card.addEventListener("click", () => {
          voiceInput.value = p.english;
          performVoiceTranslation(p.english);
        });
        phrasesContainer.appendChild(card);
      });
    } catch (err) {
      console.error(err);
    }
  }

  selCat.addEventListener("change", () => loadPhrases(selCat.value));
  loadPhrases();
}

// -----------------------------------------------------------------------------
// 4. Dictionary Search
// -----------------------------------------------------------------------------
function initDictionary() {
  const searchInput = document.getElementById("dict-search-input");
  const btnSearch = document.getElementById("btn-dict-search");
  const resultsContainer = document.getElementById("dict-results");

  async function performSearch() {
    const q = searchInput.value.trim();
    if (!q) return;

    resultsContainer.innerHTML = "<p>Searching dictionary...</p>";
    try {
      const res = await fetch(`/api/lookup?q=${encodeURIComponent(q)}`);
      const data = await res.json();
      resultsContainer.innerHTML = "";

      const items = [];
      if (data.result) items.push(data.result);
      if (Array.isArray(data.matches)) {
        items.push(...data.matches);
      }

      if (items.length === 0) {
        resultsContainer.innerHTML = `<p class="placeholder-msg">No words found for '${q}'. Try a different term.</p>`;
        return;
      }

      items.forEach((w) => {
        const card = document.createElement("div");
        card.className = "word-card";
        card.innerHTML = `
          <div class="word-header">
            <span class="word-lemma">${w.garhwali}</span>
            <span class="word-pos">${w.pos || "word"}</span>
          </div>
          <div class="word-en">${w.english || "—"}</div>
          <div class="word-hi">${w.hindi || "—"}</div>
          <div class="word-cat">Category: ${w.category || "general"}</div>
        `;
        resultsContainer.appendChild(card);
      });
    } catch (err) {
      resultsContainer.innerHTML = `<p class="placeholder-msg">Search failed: ${err}</p>`;
    }
  }

  btnSearch.addEventListener("click", performSearch);
  searchInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") performSearch();
  });
}

// -----------------------------------------------------------------------------
// 5. Verb Conjugator
// -----------------------------------------------------------------------------
function initConjugator() {
  const verbInput = document.getElementById("verb-input");
  const tenseSelect = document.getElementById("verb-tense");
  const personSelect = document.getElementById("verb-person");
  const genderSelect = document.getElementById("verb-gender");
  const btnConjugate = document.getElementById("btn-conjugate");

  const outText = document.getElementById("conjugate-output-text");
  const outSub = document.getElementById("conjugate-output-sub");

  async function performConjugation() {
    const verb = verbInput.value.trim();
    if (!verb) return;

    try {
      const url = `/api/conjugate?verb=${encodeURIComponent(verb)}&tense=${encodeURIComponent(tenseSelect.value)}&person=${personSelect.value}&gender=${genderSelect.value}`;
      const res = await fetch(url);
      const data = await res.json();
      outText.textContent = data.result;
      const gStr = genderSelect.value === "m" ? "Masculine" : "Feminine";
      outSub.textContent = `${personSelect.value} Person Singular ${gStr} • ${tenseSelect.options[tenseSelect.selectedIndex].text}`;
    } catch (err) {
      outText.textContent = "Error";
      outSub.textContent = String(err);
    }
  }

  btnConjugate.addEventListener("click", performConjugation);
}

// -----------------------------------------------------------------------------
// 6. Number Converter
// -----------------------------------------------------------------------------
function initNumbers() {
  const numInput = document.getElementById("num-input");
  const btnConvert = document.getElementById("btn-convert-num");

  const devWords = document.getElementById("num-dev-words");
  const romWords = document.getElementById("num-rom-words");
  const devDigits = document.getElementById("num-dev-digits");
  const ordText = document.getElementById("num-ordinal");

  async function performConversion() {
    const n = numInput.value.trim();
    if (!n) return;

    try {
      const res = await fetch(`/api/number?n=${encodeURIComponent(n)}`);
      const data = await res.json();
      devWords.textContent = data.devanagari_words;
      romWords.textContent = data.romanized_words;
      devDigits.textContent = data.devanagari_numerals;
      ordText.textContent = data.ordinal;
    } catch (err) {
      console.error(err);
    }
  }

  btnConvert.addEventListener("click", performConversion);
  numInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") performConversion();
  });
}

// -----------------------------------------------------------------------------
// 7. Folklore & Classical Holi
// -----------------------------------------------------------------------------
function initFolklore() {
  const formSelect = document.getElementById("holi-form");
  const btnRandomProv = document.getElementById("btn-random-proverb");
  const provBanner = document.getElementById("proverb-banner");
  const provPakhana = document.getElementById("prov-pakhana");
  const provMeaning = document.getElementById("prov-meaning");
  const songsGrid = document.getElementById("holi-songs-grid");

  async function loadHoliSongs() {
    try {
      const formVal = formSelect.value;
      const url = formVal ? `/api/folklore/holi?form=${encodeURIComponent(formVal)}` : "/api/folklore/holi";
      const res = await fetch(url);
      const data = await res.json();
      songsGrid.innerHTML = "";

      (data.holi_songs || []).forEach((s) => {
        const card = document.createElement("div");
        card.className = "song-card";
        const versesHtml = (s.verses || []).map((v) => `<div>${v}</div>`).join("");
        card.innerHTML = `
          <div class="song-title">${s.title}</div>
          <div class="song-meta-row">
            <span class="badge-tag">${s.form}</span>
            <span class="badge-tag">Raag ${s.raag}</span>
          </div>
          <div class="song-verse">${versesHtml}</div>
          <div class="song-transl">${s.english_translation}</div>
        `;
        songsGrid.appendChild(card);
      });
    } catch (err) {
      console.error(err);
    }
  }

  async function fetchRandomProverb() {
    try {
      const res = await fetch("/api/proverb/random");
      const data = await res.json();
      if (data.proverb) {
        provBanner.style.display = "block";
        provPakhana.textContent = `“${data.proverb.pakhana}”`;
        provMeaning.textContent = `Meaning: ${data.proverb.meaning} (${data.proverb.hindi})`;
      }
    } catch (err) {
      console.error(err);
    }
  }

  formSelect.addEventListener("change", loadHoliSongs);
  btnRandomProv.addEventListener("click", fetchRandomProverb);

  loadHoliSongs();
}

// -----------------------------------------------------------------------------
// 8. Digital Reader
// -----------------------------------------------------------------------------
function initReader() {
  const selBook = document.getElementById("reader-book-select");
  const inputPage = document.getElementById("reader-page-num");
  const btnRead = document.getElementById("btn-read-page");
  const btnPrev = document.getElementById("btn-prev-page");
  const btnNext = document.getElementById("btn-next-page");
  const metaBox = document.getElementById("reader-book-meta");
  const contentBox = document.getElementById("reader-page-content");
  const pageIndicator = document.getElementById("page-indicator");

  let currentBookId = "";
  let totalPages = 1;

  async function loadBooks() {
    try {
      const res = await fetch("/api/books");
      const data = await res.json();
      selBook.innerHTML = "";
      (data.books || []).forEach((b) => {
        const opt = document.createElement("option");
        opt.value = b.id;
        opt.textContent = `${b.title} (${b.year || "Historical"}) — ${b.total_pages} Pgs`;
        opt.setAttribute("data-pages", b.total_pages);
        opt.setAttribute("data-author", b.author || "");
        selBook.appendChild(opt);
      });

      if (data.books && data.books.length > 0) {
        currentBookId = data.books[0].id;
        totalPages = data.books[0].total_pages;
        loadPage(currentBookId, 1);
      }
    } catch (err) {
      console.error(err);
    }
  }

  async function loadPage(bookId, pageNum) {
    if (!bookId) return;
    contentBox.textContent = "Loading page text from digitized archives...";
    try {
      const res = await fetch(`/api/books/page?id=${encodeURIComponent(bookId)}&page=${pageNum}`);
      const data = await res.json();
      if (data.page) {
        contentBox.textContent = data.page.text || "[Blank Page]";
        pageIndicator.textContent = `Page ${pageNum} of ${totalPages}`;
        inputPage.value = pageNum;
        const opt = selBook.options[selBook.selectedIndex];
        metaBox.textContent = `Book: ${opt.textContent} • Preserved Historical Source`;
      } else {
        contentBox.textContent = `Page ${pageNum} could not be retrieved.`;
      }
    } catch (err) {
      contentBox.textContent = `Error reading page: ${err}`;
    }
  }

  selBook.addEventListener("change", () => {
    currentBookId = selBook.value;
    const opt = selBook.options[selBook.selectedIndex];
    totalPages = parseInt(opt.getAttribute("data-pages") || "1", 10);
    inputPage.max = totalPages;
    loadPage(currentBookId, 1);
  });

  btnRead.addEventListener("click", () => {
    const p = parseInt(inputPage.value, 10) || 1;
    loadPage(currentBookId, p);
  });

  btnPrev.addEventListener("click", () => {
    let p = parseInt(inputPage.value, 10) || 1;
    if (p > 1) {
      p--;
      loadPage(currentBookId, p);
    }
  });

  btnNext.addEventListener("click", () => {
    let p = parseInt(inputPage.value, 10) || 1;
    if (p < totalPages) {
      p++;
      loadPage(currentBookId, p);
    }
  });

  loadBooks();
}
