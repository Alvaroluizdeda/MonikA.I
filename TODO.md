# MonikAI - API Adaptation

## Objetivo
Adaptar o MonikAI para o novo backend do text-generation-webui usando API em vez de Playwright.

---

## Descobertas

- O backend antigo usa Playwright para controlar o navegador.
- O ponto principal está em `main.py`.

### Funções importantes

- [ ] launch()
- [ ] post_message()
- [ ] check_generation_complete()
- [ ] get_last_message()

---

## Fluxo atual

launch()
↓

post_message()
↓

check_generation_complete()
↓

get_last_message()

---

## Próximos passos

- [ ] Estudar a API do novo text-generation-webui
- [ ] Fazer um script Python simples usando a API
- [ ] Substituir o backend antigo
- [ ] Testar