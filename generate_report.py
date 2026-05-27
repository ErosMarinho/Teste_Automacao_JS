from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

OUTPUT = "relatorio_estrategia.pdf"

content = []
styles = getSampleStyleSheet()
# usar nomes de estilo personalizados para evitar colisões com estilos padrão
if 'CustomHeading1' not in styles:
    styles.add(ParagraphStyle(name='CustomHeading1', fontSize=18, leading=22, spaceAfter=12))
if 'CustomHeading2' not in styles:
    styles.add(ParagraphStyle(name='CustomHeading2', fontSize=14, leading=18, spaceAfter=8))
if 'CustomBody' not in styles:
    styles.add(ParagraphStyle(name='CustomBody', fontSize=11, leading=14))

def add_title(text):
    content.append(Paragraph(text, styles['CustomHeading1']))

def add_subtitle(text):
    content.append(Paragraph(text, styles['CustomHeading2']))

def add_paragraph(text):
    # simple line breaks handling
    for para in text.split('\n\n'):
        content.append(Paragraph(para.replace('\n', '<br/>'), styles['CustomBody']))
        content.append(Spacer(1, 8))

report_text = {
    'resumo': "Este documento apresenta um direcionamento inicial para a estratégia de testes automatizados do projeto. Aborda: escopo (UI, API, Mobile), pirâmide de testes aplicada e mapeamento de prioridades e partes críticas.",
    'estrategia': "Objetivo: agregar confiança rápida ao ciclo de desenvolvimento, reduzir regressões e acelerar entregas.\n\nAbordagens:\n- UI: automação de interface apenas para fluxos críticos de ponta a ponta (E2E) e validações visuais. Ex.: testes de fluxo de compra, login e recuperação de senha.\n- API: foco principal; testar contratos, cenários felizes e casos de erro. Usar testes isolados (unit + integration) para validação de regras e contratos.\n- Mobile: avaliar depois da estabilização do backend e UI web; priorizar testes em emuladores para fluxos críticos e smoke tests em dispositivos reais quando possível.",
    'piramide': "Base (Unit tests): 60% — testes rápidos, isolados, grandes volumes; cobrem lógica de negócio, helpers e utilitários.\nMeio (Integration / API): 30% — testes que exercitam pontos de integração, contratos, persistência e validação de serviços.\nTopo (E2E / UI): 10% — poucos testes E2E cobrindo fluxos críticos e regressões visuais.\n\nObservações: Priorizar testes de API sobre UI para obter velocidade e confiabilidade. Usar mocks/stubs quando integrar depender de serviços instáveis ou custos altos.",
    'mapeamento': "Alta Prioridade (automação imediata):\n- Fluxos de autenticação (login, logout, recuperação de senha).\n- Validações de entrada críticas (CPF, e-mail, regras de negócio principais).\n- APIs de pagamento e checkout (se aplicável).\n- Endpoints públicos e contratos (compatibilidade / regressão).\n\nMédia Prioridade: Fluxos de navegação principais do produto; Integrações com serviços terceirizados (notificações, emails).\n\nBaixa Prioridade: Visualizações secundárias, páginas com baixo tráfego, experimentos A/B.",
    'recomendacoes': "Estrutura de pastas clara: tests/unit, tests/integration, tests/e2e.\nPipelines CI separados por tipo de teste (unit -> integration -> e2e). E2E em paralelo e condicional.\nTest data e ambientes isolados: usar fixtures, factories e bancos temporários.\nFerramentas sugeridas: Unit: Jest; API: Supertest/axios + jest; E2E: Playwright ou Cypress.",
    'metricas': "Cobertura mínima orientada por risco: 80% unit nos módulos críticos.\nTempo médio de execução: manter os testes unitários < 2 minutos em CI; E2E isolados e limitados.\nFalhas por bloco: rastrear tendência de falhas por suite (flaky detection).",
    'plano': "1. Cobertura rápida de unit tests para utilitários e validações (utils/, src/scripts/validate*).\n2. Automatizar testes API para endpoints expostos e casos de validação.\n3. Criar 3-5 E2E cobrindo login, fluxo principal e validação de CPF/email.\n4. Integrar execuções no CI em etapas e configurar alertas para regressões."
}

add_title('Relatório de Estratégia de Automação')
add_subtitle('Resumo')
add_paragraph(report_text['resumo'])

add_subtitle('1. Estratégia de Automação')
add_paragraph(report_text['estrategia'])

add_subtitle('2. Pirâmide de Testes Aplicada')
add_paragraph(report_text['piramide'])

add_subtitle('3. Mapeamento de Prioridades e Partes Críticas')
add_paragraph(report_text['mapeamento'])

add_subtitle('Recomendações de Arquitetura de Testes')
add_paragraph(report_text['recomendacoes'])

add_subtitle('Métricas e Critérios de Qualidade')
add_paragraph(report_text['metricas'])

add_subtitle('Plano inicial de execução')
add_paragraph(report_text['plano'])

add_paragraph('\nDocumento gerado automaticamente: use o script generate_report.py para gerar o PDF relatorio_estrategia.pdf.')


doc = SimpleDocTemplate(OUTPUT, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=60, bottomMargin=40)
doc.build(content)
print(f'PDF gerado: {OUTPUT}')
