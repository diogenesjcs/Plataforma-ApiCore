from database import Base
from uuid import uuid4
from core.temporal.models import TemporalModelMixin
import sqlalchemy.dialects.postgresql as sap
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import *
from datetime import datetime

def get_db_name():
    return "apicore"


class domain_model(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, system_id=None,model_name=None,model=None,version=None, _metadata=None, branch='master', **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.system_id = system_id
        self.model_name = model_name
        self.model = model
        self.version = version
        self._metadata = _metadata
        self.branch = branch 

    def dict(self):
        return {
            "system_id": self.system_id,"model_name": self.model_name,"model": self.model,"version": self.version,
            "id": self.id,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'system_id','model_name','model','version', )

    system_id = Column(sap.UUID(as_uuid=True))
    model_name = Column(String)
    model = Column(String)
    version = Column(String)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class event(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, name=None,direction=None,operation_id=None,process_id=None,system_id=None,presentation_id=None, _metadata=None, branch='master', **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.name = name
        self.direction = direction
        self.operation_id = operation_id
        self.process_id = process_id
        self.system_id = system_id
        self.presentation_id = presentation_id
        self._metadata = _metadata
        self.branch = branch 

    def dict(self):
        return {
            "name": self.name,"direction": self.direction,"operation_id": self.operation_id,"process_id": self.process_id,"system_id": self.system_id,"presentation_id": self.presentation_id,
            "id": self.id,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'name','direction','operation_id','process_id','system_id','presentation_id', )

    name = Column(String)
    direction = Column(String)
    operation_id = Column(sap.UUID(as_uuid=True))
    process_id = Column(sap.UUID(as_uuid=True))
    system_id = Column(sap.UUID(as_uuid=True))
    presentation_id = Column(sap.UUID(as_uuid=True))

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class installed_apps(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, system_id=None,host=None,name=None,port=None,type=None, _metadata=None, branch='master', **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.system_id = system_id
        self.host = host
        self.name = name
        self.port = port
        self.type = type
        self._metadata = _metadata
        self.branch = branch 

    def dict(self):
        return {
            "system_id": self.system_id,"host": self.host,"name": self.name,"port": self.port,"type": self.type,
            "id": self.id,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'system_id','host','name','port','type', )

    system_id = Column(sap.UUID(as_uuid=True))
    host = Column(String)
    name = Column(String)
    port = Column(Integer)
    type = Column(String)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class map(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, system_id=None,process_id=None,name=None,content=None, _metadata=None, branch='master', **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.system_id = system_id
        self.process_id = process_id
        self.name = name
        self.content = content
        self._metadata = _metadata
        self.branch = branch 

    def dict(self):
        return {
            "system_id": self.system_id,"process_id": self.process_id,"name": self.name,"content": self.content,
            "id": self.id,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'system_id','process_id','name','content', )

    system_id = Column(sap.UUID(as_uuid=True))
    process_id = Column(sap.UUID(as_uuid=True))
    name = Column(String)
    content = Column(Text)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class operation(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, name=None,process_id=None,system_id=None,event_in=None,event_out=None,image=None,commit=None, _metadata=None, branch='master', **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.name = name
        self.process_id = process_id
        self.system_id = system_id
        self.event_in = event_in
        self.event_out = event_out
        self.image = image
        self.commit = commit
        self._metadata = _metadata
        self.branch = branch 

    def dict(self):
        return {
            "name": self.name,"process_id": self.process_id,"system_id": self.system_id,"event_in": self.event_in,"event_out": self.event_out,"image": self.image,"commit": self.commit,
            "id": self.id,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'name','process_id','system_id','event_in','event_out','image','commit', )

    name = Column(String)
    process_id = Column(sap.UUID(as_uuid=True))
    system_id = Column(sap.UUID(as_uuid=True))
    event_in = Column(String)
    event_out = Column(String)
    image = Column(String)
    commit = Column(Boolean)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class operation_instance(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, status=None,must_commit=None,process_instance_id=None,process_id=None,system_id=None,operation_id=None,image=None,event_name=None, _metadata=None, branch='master', **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.status = status
        self.must_commit = must_commit
        self.process_instance_id = process_instance_id
        self.process_id = process_id
        self.system_id = system_id
        self.operation_id = operation_id
        self.image = image
        self.event_name = event_name
        self._metadata = _metadata
        self.branch = branch 

    def dict(self):
        return {
            "status": self.status,"must_commit": self.must_commit,"process_instance_id": self.process_instance_id,"process_id": self.process_id,"system_id": self.system_id,"operation_id": self.operation_id,"image": self.image,"event_name": self.event_name,
            "id": self.id,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'status','must_commit','process_instance_id','process_id','system_id','operation_id','image','event_name', )

    status = Column(String)
    must_commit = Column(Boolean)
    process_instance_id = Column(sap.UUID(as_uuid=True))
    process_id = Column(sap.UUID(as_uuid=True))
    system_id = Column(sap.UUID(as_uuid=True))
    operation_id = Column(sap.UUID(as_uuid=True))
    image = Column(String)
    event_name = Column(String)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class presentation(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, name=None,url=None,system_id=None, _metadata=None, branch='master', **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.name = name
        self.url = url
        self.system_id = system_id
        self._metadata = _metadata
        self.branch = branch 

    def dict(self):
        return {
            "name": self.name,"url": self.url,"system_id": self.system_id,
            "id": self.id,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'name','url','system_id', )

    name = Column(String)
    url = Column(String)
    system_id = Column(sap.UUID(as_uuid=True))

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class presentation_instance(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, presentation_id=None,system_id=None, _metadata=None, branch='master', **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.presentation_id = presentation_id
        self.system_id = system_id
        self._metadata = _metadata
        self.branch = branch 

    def dict(self):
        return {
            "presentation_id": self.presentation_id,"system_id": self.system_id,
            "id": self.id,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'presentation_id','system_id', )

    presentation_id = Column(sap.UUID(as_uuid=True))
    system_id = Column(sap.UUID(as_uuid=True))

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class process(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, name=None,relative_path=None,deploy_date=None,tag=None,image_id=None,system_id=None, _metadata=None, branch='master', **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.name = name
        self.relative_path = relative_path
        self.deploy_date = deploy_date
        self.tag = tag
        self.image_id = image_id
        self.system_id = system_id
        self._metadata = _metadata
        self.branch = branch 

    def dict(self):
        return {
            "name": self.name,"relative_path": self.relative_path,"deploy_date": self.deploy_date,"tag": self.tag,"image_id": self.image_id,"system_id": self.system_id,
            "id": self.id,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'name','relative_path','deploy_date','tag','image_id','system_id', )

    name = Column(String)
    relative_path = Column(String)
    deploy_date = Column(DateTime)
    tag = Column(String)
    image_id = Column(String)
    system_id = Column(sap.UUID(as_uuid=True))

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class process_instance(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, start_execution=None,end_execution=None,reference_date=None,status=None,process_id=None,origin_event_name=None,system_id=None, _metadata=None, branch='master', **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.start_execution = start_execution
        self.end_execution = end_execution
        self.reference_date = reference_date
        self.status = status
        self.process_id = process_id
        self.origin_event_name = origin_event_name
        self.system_id = system_id
        self._metadata = _metadata
        self.branch = branch 

    def dict(self):
        return {
            "start_execution": self.start_execution,"end_execution": self.end_execution,"reference_date": self.reference_date,"status": self.status,"process_id": self.process_id,"origin_event_name": self.origin_event_name,"system_id": self.system_id,
            "id": self.id,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'start_execution','end_execution','reference_date','status','process_id','origin_event_name','system_id', )

    start_execution = Column(DateTime)
    end_execution = Column(DateTime)
    reference_date = Column(DateTime)
    status = Column(String)
    process_id = Column(sap.UUID(as_uuid=True))
    origin_event_name = Column(String)
    system_id = Column(sap.UUID(as_uuid=True))

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class reproduction(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, system_id=None,process_id=None,original_instance_id=None,instance_id=None,owner=None,external_id=None,execution_start_date=None, _metadata=None, branch='master', **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.system_id = system_id
        self.process_id = process_id
        self.original_instance_id = original_instance_id
        self.instance_id = instance_id
        self.owner = owner
        self.external_id = external_id
        self.execution_start_date = execution_start_date
        self._metadata = _metadata
        self.branch = branch 

    def dict(self):
        return {
            "system_id": self.system_id,"process_id": self.process_id,"original_instance_id": self.original_instance_id,"instance_id": self.instance_id,"owner": self.owner,"external_id": self.external_id,"execution_start_date": self.execution_start_date,
            "id": self.id,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'system_id','process_id','original_instance_id','instance_id','owner','external_id','execution_start_date', )

    system_id = Column(sap.UUID(as_uuid=True))
    process_id = Column(sap.UUID(as_uuid=True))
    original_instance_id = Column(sap.UUID(as_uuid=True))
    instance_id = Column(sap.UUID(as_uuid=True))
    owner = Column(String)
    external_id = Column(String)
    execution_start_date = Column(DateTime)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class sent_event(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, event_id=None,presentation_instance_id=None,operation_instance_id=None,event_date=None,reference_date=None,payload=None,is_reproduction=None, _metadata=None, branch='master', **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.event_id = event_id
        self.presentation_instance_id = presentation_instance_id
        self.operation_instance_id = operation_instance_id
        self.event_date = event_date
        self.reference_date = reference_date
        self.payload = payload
        self.is_reproduction = is_reproduction
        self._metadata = _metadata
        self.branch = branch 

    def dict(self):
        return {
            "event_id": self.event_id,"presentation_instance_id": self.presentation_instance_id,"operation_instance_id": self.operation_instance_id,"event_date": self.event_date,"reference_date": self.reference_date,"payload": self.payload,"is_reproduction": self.is_reproduction,
            "id": self.id,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'event_id','presentation_instance_id','operation_instance_id','event_date','reference_date','payload','is_reproduction', )

    event_id = Column(sap.UUID(as_uuid=True))
    presentation_instance_id = Column(sap.UUID(as_uuid=True))
    operation_instance_id = Column(sap.UUID(as_uuid=True))
    event_date = Column(Date)
    reference_date = Column(Date)
    payload = Column(Text)
    is_reproduction = Column(Boolean)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class system(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, name=None,description=None,version=None, _metadata=None, branch='master', **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.name = name
        self.description = description
        self.version = version
        self._metadata = _metadata
        self.branch = branch 

    def dict(self):
        return {
            "name": self.name,"description": self.description,"version": self.version,
            "id": self.id,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'name','description','version', )

    name = Column(String)
    description = Column(String)
    version = Column(String)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)






