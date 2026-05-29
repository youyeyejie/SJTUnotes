window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  },
  output: {
    displayOverflow: "linebreak",
    linebreaks: {
      inline: true,
      width: "100%"
    }
  },
  startup: {
    ready() {
      MathJax.startup.defaultReady();

      const renderMath = () => {
        MathJax.startup.promise = MathJax.startup.promise
          .then(() => {
            MathJax.typesetClear();
            MathJax.texReset();
            return MathJax.typesetPromise();
          })
          .catch((error) => console.error("MathJax render failed:", error));
      };

      if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", renderMath, { once: true });
      } else {
        renderMath();
      }

      if (typeof document$ !== "undefined" && document$.subscribe) {
        document$.subscribe(() => {
          renderMath();
        });
      }
    }
  }
};
