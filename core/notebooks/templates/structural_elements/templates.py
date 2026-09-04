import textwrap


class Templates:
    @staticmethod
    def header_title() -> str:
        return textwrap.dedent("""
            <div style="
                box-shadow:
                    inset #444 0 0 0 5px,
                    inset #333 0 0 0 1px,
                    inset #555 0 0 0 10px,
                    inset #666 0 0 0 11px,
                    inset #888 0 0 0 16px,
                    inset #777 0 0 0 17px,
                    inset #ddd 0 0 0 21px,
                    inset #ccc 0 0 0 22px;
                padding: 50px"
            >

            <h1 style="
                text-align: center;
                margin-bottom: 50px"
            >
                Разработка решения МО для «ООО КОМПАНИЯ»
            </h1>
        """).strip()

    @staticmethod
    def header_project_description_examples():
        return textwrap.dedent("""
            Пример 1:
            Заказчик в лице компании нуждается в имитации 
            технологического процесса ... для экономии ... 
            Сам процесс можно логически разделить на 
            несколько важных аспектов: список
                    
            Пример 2 временный ряд:
                    
            Компании требуется решение проблемы... 
            Для решения проблемы выбран подход...,
            поэтому решать проблему начинаем с анализа 
            исторических данных, предоставляемых компанией, 
            затем плавно переходим к автоматизации процесса 
            с помощью машинного обучения.
                    
            Пример 3:
            Руководство ставит перед собой цель...
            поэтому отдел сконцентрирован на ...
                    
            Пример 4:
            Мне передали данные о ... для построения моделей,
            которые помогут... эффективному расширению бизнеса
            заказчика с удержанием определённых критериев: список
                    
            Пример 5: 
            метрикой успеха было определено... Для достижения цели компания
            планирует разработать систему, которая сможет точно определять ...
                    
            Создание такой модели оценки стоимости позволит...
            Метрика "привлечение новых клиентов" в технической части 
            делится на 3 важных критерия: список
        """).strip()

    @staticmethod
    def header_goal_section() -> str:
        return textwrap.dedent("""
            <div style="
                background: #666;
                color: #fff;
                text-align: center;
                font-weight: 600;
                margin-top: 20px;
            ">
                1. &nbsp; &nbsp; &nbsp; Цель
            </div>
            <br>
            
            Пример 1:
            По карте технологического процесса разработать модель машинного
            обучения, которая будет предсказывать целевой признак...
            Целевой изменяется на протяжении всего технологического 
            процесса из-за... Эти изменения должны быть предсказуемы, 
            чтобы можно было управлять процессом.
                    
            Пример 2:
            Цель исследования установлена с учетом запроса от ООО КОМПАНИЯ. 
            В первую очередь заказчик выражает интерес...
                    
            Пример 3:
            Руководитель отдела сформировал подход к решению задачи:...
                    
            Пример 4:
            Добиться наилучших оценок в описанных ранее критериях метрики успеха
            путём построения и выбора моделей под задачу       
            
        """)

    @staticmethod
    def header_source_data_section_title() -> str:
        return textwrap.dedent("""
            <div style="
                background: #666;
                color: #fff;
                text-align: center;
                font-weight: 600;
                margin-top: 20px;
            ">
                2. &nbsp; &nbsp; &nbsp; Исходные данные: структура и вызовы
            </div>
        """).strip()

    @staticmethod
    def header_action_plan_section() -> str:
        return textwrap.dedent("""
            <div style="
                background: #666;
                color: #fff;
                text-align: center;
                font-weight: 600;
                margin-top: 20px;
            ">
                4. &nbsp; &nbsp; &nbsp; План действий
            </div>

            - [ ] Загрузите данные и выполните их ресемплирование по одному часу;
            - [x] Файл с данными открыт.
            
            </div>
        """).strip()

    @staticmethod
    def load_data() -> str:
        return textwrap.dedent("""
            **Новая структура данных:**
            
            - **Нагреватели**    
            - `id` — описание;
            <br> <br>  
                
            - **Целевой признак**
            - `id` — описание;
            - `target` - описание;
            <br> <br>  
        """).strip()

    @staticmethod
    def general_conclusion() -> str:
        return textwrap.dedent("""
            --- 
            **Аномалии:** 
            - a. ;
            - b. ;
            - c. ;
            
            **Причины:** 
            - a. ;
            - b. ;
            - c. ;
            
            **Методы устранения:** 
            - a. ;
            - b. ;
            - c. ;
            --- 
            
            **Дубликаты:** 
            - Отсутствуют
            --- 
        """).strip()

    @staticmethod
    def data_optimization() -> str:
        return textwrap.dedent("""
            Обработка

            **Почему типы данных были изменены?**
            - `total_images` - никто не будет добавлять огромное количество фотографий
              к недвижимости, поэтому мы ограничились 255 фотографиями.
              Само количество фотографий не может быть отрицательным;
        """).strip()

    @staticmethod
    def heatmap_code() -> str:
        return textwrap.dedent("""
            transform_autos_v_1_temp = transform_autos_v_1.copy()
    
            interval_cols = [
                'price', 'power', 'kilometer',
            ]
    
            phik_corr_matrix = (
                transform_autos_v_1_temp
                .drop(
                    columns=[
                        'date_crawled',
                        'date_created',
                        'last_seen'
                    ],
                    axis=1
                )
                .sample(500)
                .phik_matrix(interval_cols=interval_cols)
            )
    
            plt.figure(figsize=(14, 7))
    
            sns.heatmap(
                phik_corr_matrix,
                annot=True,
                cmap="YlGn"
            )
    
            plt.title('Хитмап')
            plt.show()
        """).strip()

    @staticmethod
    def correlation_conclusion() -> str:
        return textwrap.dedent("""
            По матрице мы видим такие корреляции:
            
            * `price` c `registration_year`, `model`, `postal_code`, `big_mileage`;
            * `vehicle_type` с `postal_code`, `model`, `power`, `brand`, `registration_year`;
            * `registration_year` с `kilometer`
              (логично, что лучше, чем `big_mileage`, так как более точная);
            * `gearbox` с `power` и `model`;
            * `power` с `postal_code`, `brand`, `model`, `gearbox`, `vehicle_type`;
            * `postal_code` с `big_mileage`, `brand`, `fuel_type`,
              `registration_month`, `model`, `power`, `vehicle_type`, `price`.
            
            `registration_year` в целом включает в себя и модель, и пробег,
            потому что чем больше времени проходит, тем лучше выпускаются машины,
            а новые машины всегда стоят дороже. Но параметр `kilometer` хуже
            настраивает `price`, поэтому, возможно, в совокупности с остальными
            параметрами из `registration_year` он сможет даже лучшую корреляцию выдать.
            
            Чинилась машина или нет особо никого не волнует: смотря машины
            с пробегом, люди готовы увидеть машину после ремонта.
            
            Также нужно попробовать поточнее настроить параметр `old_car`
            через scatter plot.
            
            `postal_code` неожиданно оказался крайне интересным параметром.
            Оказывается, он напрямую передаёт фактор геолокации с учётом всех
            особенностей.
            
            То есть его зависимость с `model` говорит о труднодоступности
            покупки машины за границей или же о том, что люди чаще выбирают
            отечественные марки.
            
            Зависимость параметра с `big_mileage` говорит о том, что фактор
            учитывает, где находилась машина: если это маленький город —
            машина используется не так сильно, как в большом городе; если
            город большой и не мегаполис, где всё удобно и под рукой, то она
            используется очень плотно.
            
            Даже тип топлива оказался повязанным с `postal_code`, правда,
            нам это скорее не на руку, так как с `price` он дел иметь не желает.
            
            Также балансирует `power`, `model` и `vehicle_type`, но они там
            между собой повязаны, поэтому расплетать их — долгая история.
            Слишком плотный параметр, где много чего лишнего.
            
            `registration_month` сильно коррелирует с `postal_code`,
            видимо, есть какие-то непонятные особенности, о которых
            я, к сожалению, не могу знать.
            
            Я бы провёл достаточно большую инженерию данных, потому что признаки
            сильно перемешаны друг с другом, а с `price` коррелируют не все.
            
            Тип кузова `vehicle_type` очень сильно зависит от местности
            `postal_code`, видимо, поэтому сам по себе сильной зависимости
            с `price` он не даёт.
            
            Есть интересная зависимость коробки передач с моделью и мощностью,
            но её смысла рассматривать нет, потому что по сути цена зависит
            от коробки только потому, что она зависит от модели, в которую
            также входит мощность. Следовательно, модель — основной объединённый
            параметр для этого.
            
            Но модель настолько сильно зависит от `postal_code`,
            что даже сложно сказать, что лучше выбрать.
            
            Сам по себе год регистрации роль не играет, играет только за счёт того,
            что несёт в себе модель и пробег, поэтому его лучше не использовать.
            
            Очень интересно, что мощность никак не связана с пробегом.
            
            Нужно учитывать, что модель не учитывает напрямую год выпуска,
            потому что можно купить модель одного года выпуска, а можно другого,
            раз уж там не полная зависимость.
            
            Выходит такая схема для признака:
            
            `model` or `brand`, `big_mileage`, `old_car`, `repaired`
            
            `big_mileage`, `old_car`, `power`, `vehicle_type`,
            `gearbox`, `brand`, `repaired`
        """).strip()

    @staticmethod
    def big_engineering() -> str:
        return textwrap.dedent("""
            print(
                'Изначальные размеры таблицы нагревателей:',
                heaters.shape
            )
            
            print(
                'Изначальные размеры таблицы объёмов сыпучих материалов:',
                bulk_volume.shape
            )
            
            dataframe = heaters.merge(bulk_volume, on="batch_id", how="inner")
            
            print(
                'Размер конечной таблицы:',
                dataframe.shape
            )
            
            columns_to_check = ["bulk_" + str(i) for i in range(1, 16)]
            
            missing_rows_all = dataframe[dataframe[columns_to_check].isna().all(axis=1)]
            
            print("Число строк, где все указанные столбцы NaN:", missing_rows_all.shape[0])
            print('Список индентификаторов партий, в которых не добавлялись сыпучие материалы:')
            print(missing_rows_all['batch_id'].values)
            
            batch_ids_with_wire_materals = missing_rows_all['batch_id']
            
            dataframe.rename(
                columns=lambda col: 'volume_' + col if col in columns_to_check else col,
                inplace=True
            )
            
            dataframe.head(0)
        """).strip()

    @staticmethod
    def intermediate_conclusion(research_step: str) -> str:
        return textwrap.dedent(f"""
            <div style="
            color: green;
            padding: 20px;
            border: 2px dotted green;
            ">
            
            **Мы закончили выполнение {research_step} и вот что выяснили:**
            
            <ul>
            <li>
            
            **@heaters `batch_id`.**
            
            39 партий, которые имеют по 1ой записи в таблице: в таблицу попала часть другого технологического процесса. Удалить heaters_outliers
            
            На многих графиках временного ряда виден интервал, где оборудование дало сбой:
            
            - 13ого и 18ого числа слишком большие перерывы между партиями;
            - отсутствуют данные с 14 ого по 17ое включительно.
            
            Так как ситуацию удалось отследить один единый раз, то более глубокий анализ временного ряда, анализ сезонности и прочего врятле дадут нам хороший результат.
            </li>
            
            <li>
            
            **@heaters `active_power`.**
            
            Распределение имеет длинный хвост в сторону больших мощностей, соответственно есть вероятность, что какие-то определённые компоненты требуют более высокой мощности, чтобы удерживаться на той же самой температуре.
            </li>
            
            <li>
            
            **@heaters `reactive_power`.**
            
            Резкий выброс реактивной мощности в систему ещё больше наталкивает на мысль, что отключение оборудования с 13 по 18 марта вызванно поломками в системе.
            </li>
            
            <li>
            
            **@bulk_volume `bulk_1` - `bulk-15` и @wire_volume `wire_1` - `wire_9`**
            
            По каждому легирующему материалу был построен boxplot и были найдены экстремальные значения. Есть вероятность, что связано с попытками балансировать, а есть вероятность, что сами по себе требовались в большем размере. Узнать мы этого не сможем.
            </li>
            
            <li>
            
            **@bulk_time**
            
            Отвечает на вопрос: "Когда именно подали тот или иной легат?". К сожалению, ничего сверхъестественного мы получить здесь не можем.
            
            Пропуски заполнить нулями или минимальными временными марками `pd.Timestamp.min` мы не можем, потому что полетит отображение графиков. В целом, пропуски расположены абсолютно в тех же местах, где они расположены в таблице bulk_time, поэтому можно попробовать заполнить свдигами, чтобы график был более точным, но не уверен, что это нам что-то даст, так как с пропусками он показал примерную картину.*
            
            Из этого поля мы можем получить информацию о частоте использования того или иного легирующего материала, что может стать дополнительным признаком в таблице, чтобы не усложнять модель временным рядом.
            </li>
            
            <li>
            
            **@gas_volume `volume`.**
            
            Не понятный скос распределения. 129 значений выходит за правый ус boxplot. Пока точно сказать о чём это говорит сложно.
            </li>
            
            <li>
            
            **@temperature `batch_id`.**
            
            2е партии в таблице, по которым есть всего один замер: ошибка наблюдателя или другой технический процесс. Партии повторяются. Повторений на 1 больше, чем в таблице с нагревателями: наблюдается финальный замер. Некоторые партии не повторяются: имеют постоянную температуру. Нужно привести всё к единственному значению, выбрав температуру, которая получилась в самом конце, но при этом не забыть зафиксировать начальную температуру.
            
            Также полезно добавить в модель два новых признака: среднюю температуру и начальную температуру.
            </li>
            
            <li>
            
            **@temperature `timestamp`.**
            
            Присутствуют записи ранее 2019 года без указания температур.
            </li>
            
            <li>
            
            **@temperature `temperature`.**
            
            Были замечены данные, которые соответствовали слишком низким температурам (1191–1250). 5 забракованных партий из-за длительного простоя печи.
            </li>
            </ul>
            
            **Всё зависит от того что мы хотим от модели.**
            
            1. Научить её работать на идеальном технологическом процессе.
            2. Научить её работать в ряде ошибок, которые есть в реальных данных.
            
            **В целом остались неизученные параметры (уязвимости):**
            
            <ul>
            <li>@bulk_volume `bulk_1` - `bulk-15` и @wire_volume `wire_1` - `wire_9`;</li>
            <li>@gas_volume `volume`;</li>
            <li>@temperature `timestamp`;</li>
            <li>@temperature `temperature`.</li>
            </ul>
            
            </div>
        """).strip()

    @staticmethod
    def metrics_for_digit_parameter(df_name, column) -> str:
        return f'{df_name}["{column}"].describe(include="all")'

    @staticmethod
    def metrics_for_id_parameter(df_name) -> str:
        return textwrap.dedent(f"""
                print(
                    'Статистика:',
                    {df_name}['id'].describe(include="all"),
                )
                print()
                
                duplicates = (
                    {df_name}[{df_name}['id'].duplicated()]['id']
                    .value_counts()
                )
                
                print(
                    'Максимальное число записей по одной партии в таблице целевого признака =',
                    duplicates.max(),
                )
                print()
                print(
                    'Среднее число записей по одной партии в таблице =',
                    duplicates.mean()
                )
                
                print()
                
                non_repeated = {df_name}['id'].value_counts()
                non_repeated = non_repeated[non_repeated == 1].index
                
                print(
                    "id, которые не повторялись в DataFrame:", 
                    len(list(non_repeated))
                )
            """).strip()

    @staticmethod
    def metrics_for_timeseries_parameter(df_name, column) -> str:
        return textwrap.dedent(f"""
            print(
                'Данные начинаются с -',
                {df_name}['{column}'].min()
            )
            print(
                'Данные заканчиваюся -',
                {df_name}['{column}'].max(),
            )
            print(
                'Уникальных дат относительно всех',
                {df_name}['{column}'].nunique() / len({df_name}['{column}']),
            )
            print(
                'Оценка сезонности:',
                ({df_name}['{column}'].value_counts())[:5],
                '',
                sep='\\n'
            )
            
            # среднее время между нагреваниями по одной партии
            time_diff = {df_name}.groupby('id')['{column}'].diff()
            
            average_time_between_heatings = time_diff.median()
            
            print(
                'Среднее время между записями в журнал в рамках одной партии =',
                average_time_between_heatings
            )
            # среднее время между партиями
            min_start_times = (
                {df_name}[['batch_id', '{column}']]
                .drop_duplicates(subset='id', keep='first')
            )
            
            min_start_times = min_start_times.set_index('id').sort_index()
            
            min_start_times['diff'] = (
                min_start_times['{column}'].shift(-1) - min_start_times['{column}']
            )
            
            print(
                'Среднее время, которое проходит от начала обработки'
                 'одной партии до начала другой = ',
                min_start_times['diff'].median()
            )
            
            
            # среднее количество переключений в день
            print(
                'Среднее количество переключений (или записей в журнале) в день =',
                round((
                    heaters
                    .groupby(
                        [{df_name}['{column}'].dt.month, {df_name}['{column}'].dt.day]
                    )['id']
                    .count()
                ).mean())
            )
            """).strip()
