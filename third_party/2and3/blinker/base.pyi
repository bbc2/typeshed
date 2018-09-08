from typing import (Any, Callable, ContextManager, Dict, Generator, List, Optional, Tuple,
                    TypeVar)
from weakref import WeakValueDictionary

from ._utilities import symbol

ANY: symbol

ReceiverType = Callable[..., Any]
ReceiverVar = TypeVar('ReceiverVar', bound=ReceiverType)

class Signal:
    receivers: Dict[int, ReceiverType]
    @property
    def received_connected(self) -> 'Signal': ...
    @property
    def received_disconnected(self) -> 'Signal': ...
    def __init__(self, doc: Optional[str] = ...) -> None: ...
    def connect(
            self,
            receiver: ReceiverType,
            sender: symbol = ...,
            weak: bool = ...,
    ) -> Callable[..., Any]: ...
    def connect_via(
            self,
            sender: Any,
            weak: bool = ...,
    ) -> Callable[[ReceiverVar], ReceiverVar]: ...
    def connected_to(
            self,
            receiver: ReceiverType,
            sender: Any = ...,
    ) -> ContextManager[None]: ...
    def temporarily_connected_to(
            self,
            receiver: ReceiverType,
            sender: Any = ...,
    ) -> ContextManager[None]: ...
    def send(self, *sender: Any, **kwargs: Any) -> List[Tuple[ReceiverType, Any]]: ...
    def has_receivers_for(self, sender: Any) -> bool: ...
    def receivers_for(self, sender: Any) -> Generator[None, ReceiverType, None]: ...
    def disconnect(self, receiver: ReceiverType, sender: Any = ...): ...

receiver_connected: Signal

class NamedSignal(Signal):
    def __init__(self, name: str, doc: Optional[str] = ...) -> None: ...

class Namespace(dict):
    def signal(self, name: str, doc: Optional[str] = ...) -> NamedSignal: ...

class WeakNamespace(WeakValueDictionary):
    def signal(self, name: str, doc: Optional[str] = ...) -> NamedSignal: ...

def signal(name: str, doc: Optional[str] = ...) -> NamedSignal: ...
