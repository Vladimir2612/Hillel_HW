#1 .Call test with filename (--tb=no - without traces in console)

python -m pytest -v test_base.py 
python -m pytest -v test_base.py  --tb=no

python -m pytest -v -k "ever"
python -m pytest -v -k "check" --tb=no

python -m pytest -v -k "test_first and not test_second” --tb=no
-k - runs the test based on the keyword expression
-x  - exit on first fail
--maxfail=2  - exit after 2 fails
-q - quiet mode, less logs
--co - collect test only, without run
--lf - run last-failed tests
--ff - failed first run again and then run all other tests


#2. Show prints → pytest -v tests/test_class.py - s

#3. Class → pytest -v tests/test_class.py::Testing

#4. Method in class → pytest -v tests/test_class.py::Testing::test_str

#5. Method in module → pytest -v tests/test_base.py::test_third 

#6. Markers
@pytest.mark.sanity → pytest -v tests/test_skip.py -m 'sanity'
@pytest.mark.sanity AND @pytest.mark.str →pytest -v tests/test_skip.py -m 'sanity and not str'