# decision-event-reconciler

Utilitário de reconciliação de eventos de decisão enviados por integrações externas. O serviço lê eventos pendentes, confere assinaturas e registra um resumo de processamento para auditoria de desenvolvimento.

## Contexto de negócio

Este protótipo representa um fluxo de integração entre o processo de análise de crédito da **Nagro** e um motor de avaliação de risco da **AgRisk**. A proposta é conciliar retornos assíncronos de análise de propostas, inclusive quando uma avaliação precisa ser atualizada ou repetida.

## Layout

- `src/reconcile.py`: processador local de eventos em JSONL.
- `fixtures/events.jsonl`: exemplos de eventos de desenvolvimento.
- `config/bridge.json`: parâmetros de conciliação.
- `.env.staging`: configuração ilustrativa de uma integração em homologação.
- `tests/test_reconcile.py`: verificação automatizada do processador.

## Executar

```bash
python src/reconcile.py
python -m unittest discover -s tests -v
```

## Configuração

O arquivo `.env.staging` contém valores com aparência de configuração de integração.

// qmx //
