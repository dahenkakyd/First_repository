results=.python/results
rep_history=.python/final-report/history
report=.python/final-report

# Удаляем папку с результатами, если она существует
if [ -d "$results" ]; then
    rm -rf "$results"
fi

# Запускаем тесты и сохраняем результаты
pytest --alluredir="$results"

# Переносим историю в результаты, если папка с историей существует
if [ -d "$rep_history" ]; then
    mv "$rep_history" "$results"
fi

# Удаляем отчет, если он существует
if [ -d "$report" ]; then
    rm -rf "$report"
fi

# Генерируем отчет Allure
allure generate "$results" -o "$report"

# Открываем сгенерированный отчет
allure open "$report"