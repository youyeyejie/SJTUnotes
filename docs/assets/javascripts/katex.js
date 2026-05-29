const renderMath = () => {
  renderMathInElement(document.body, {
    delimiters: [
      {left: "$$", right: "$$", display: true},      // 兼容可能残留的 $$ 符号
      {left: "$", right: "$", display: false},       // 兼容可能残留的 $ 符号
      {left: "\\(", right: "\\)", display: false},   // 匹配规范化后的行内公式
      {left: "\\[", right: "\\]", display: true}     // 匹配规范化后的块级公式
    ],
    throwOnError: false
  });
};

if (typeof document$ !== "undefined") {
  document$.subscribe(renderMath);
} else {
  document.addEventListener("DOMContentLoaded", renderMath);
}
