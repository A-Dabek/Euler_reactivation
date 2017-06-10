import importlib
import resource

NO_OF_PROBLEMS = 610


def get_solution_of(number, *args):
    assert 0 < number <= NO_OF_PROBLEMS, "Invalid problem number"
    pkg_name = str.format('p{}0s', number // 10 if number < 100 else (number // 100) * 10)
    file_name = str.format('p{}{}', '' if number < 100 else number // 100, ('0' + str(number % 10)) if (number // 10) % 10 == 0 else number % 100)
    try:
        print(resource.get_problem_info(number))
        pkg = importlib.import_module(str.format('{}.{}', pkg_name, file_name))
        time, result = resource.measure_time(pkg.solve, *args)
        return str.format('Answer: {}\nin {}s', result, time)
    except ImportError:
        return str.format('Problem {}.{} is not solved yet', pkg_name, file_name)


if __name__ == '__main__':
    problem = 549
    print(get_solution_of(problem))
