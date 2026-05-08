"use strict";

let _current = {};
let _fallback = {};

async function loadLang(lang) {
  if (Object.keys(_fallback).length === 0) {
    _fallback = await _fetchLang("en");
  }
  _current = lang === "en" ? _fallback : await _fetchLang(lang);
}

async function _fetchLang(lang) {
  try {
    const res = await fetch(`./lang/${lang}.json`);
    if (!res.ok) return {};
    return await res.json();
  } catch {
    return {};
  }
}

function t(keyPath, args = {}) {
  const keys = keyPath.split(".");
  const fromCurrent = _resolve(_current, keys);
  const str = fromCurrent ?? _resolve(_fallback, keys) ?? keyPath;
  if (!args || Object.keys(args).length === 0) return str;
  return str.replace(/\{(\w+)\}/g, (_, k) => String(args[k] ?? `{${k}}`));
}

function _resolve(obj, keys) {
  let cur = obj;
  for (const k of keys) {
    if (cur == null || typeof cur !== "object") return undefined;
    cur = cur[k];
  }
  return typeof cur === "string" ? cur : undefined;
}

function applyTranslations() {
  document.querySelectorAll("[data-i18n]").forEach((el) => {
    el.textContent = t(el.dataset.i18n);
  });
  document.querySelectorAll("[data-i18n-placeholder]").forEach((el) => {
    el.placeholder = t(el.dataset.i18nPlaceholder);
  });
  document.querySelectorAll("[data-i18n-title]").forEach((el) => {
    el.title = t(el.dataset.i18nTitle);
  });
}

export { loadLang, t, applyTranslations };
