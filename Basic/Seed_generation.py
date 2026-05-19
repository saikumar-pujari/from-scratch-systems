import random 
import contextlib
from typing import Generator, Any

@contextlib.contextmanager
def rand_state(seed: int) -> Generator[None, None, None, Any]:
    state:random.Random = random.getstate() 
    # state:Tuple[Any|None] = random.getstate() #we could go with the tuple[any|None] also instead of random.random
    random.seed(seed)
    try:
        yield
    finally:
        random.setstate(state) #saves the state

def main() -> None:
    print("Random number before context manager:", random.randint(1, 100))
    with rand_state(42):
        print("Random number inside context manager:", random.randint(1, 100))
    print("Random number after context manager:", random.randint(1, 100))

if __name__ == "__main__":
    main()
