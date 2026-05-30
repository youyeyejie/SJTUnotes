function getGiscusTheme() {
  const scheme = document.body?.dataset?.mdColorScheme;
  if (scheme === "slate") {
    return "dark";
  }
  if (scheme === "default") {
    return "light";
  }
  return "preferred_color_scheme";
}

function mountGiscus() {
  const container = document.querySelector("[data-giscus='true']");
  if (!container) {
    return;
  }

  if (container.querySelector("iframe.giscus-frame")) {
    return;
  }

  container.innerHTML = "";

  const script = document.createElement("script");
  script.src = "https://giscus.app/client.js";
  script.async = true;
  script.crossOrigin = "anonymous";

  for (const [key, value] of Object.entries(container.dataset)) {
    if (key === "giscus") {
      continue;
    }
    script.setAttribute(`data-${key.replace(/[A-Z]/g, (match) => `-${match.toLowerCase()}`)}`, value);
  }

  script.setAttribute("data-theme", getGiscusTheme());
  container.appendChild(script);
}

function updateGiscusTheme() {
  const iframe = document.querySelector("iframe.giscus-frame");
  if (!iframe?.contentWindow) {
    return;
  }

  iframe.contentWindow.postMessage(
    {
      giscus: {
        setConfig: {
          theme: getGiscusTheme()
        }
      }
    },
    "https://giscus.app"
  );
}

function initializeGiscus() {
  mountGiscus();
  updateGiscusTheme();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initializeGiscus, { once: true });
} else {
  initializeGiscus();
}

if (typeof document$ !== "undefined" && document$.subscribe) {
  document$.subscribe(() => {
    initializeGiscus();
  });
}

const giscusThemeObserver = new MutationObserver(() => {
  updateGiscusTheme();
});

if (document.body) {
  giscusThemeObserver.observe(document.body, {
    attributes: true,
    attributeFilter: ["data-md-color-scheme"]
  });
} else {
  document.addEventListener(
    "DOMContentLoaded",
    () => {
      giscusThemeObserver.observe(document.body, {
        attributes: true,
        attributeFilter: ["data-md-color-scheme"]
      });
    },
    { once: true }
  );
}
