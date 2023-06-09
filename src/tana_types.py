# Generated by https://quicktype.io
#
# To change quicktype's target language, run command:
#
#   "Set quicktype target language"

from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, Union, List, Dict, Any


class PropType(Enum):
  ASSOCIATED_DATA = "associatedData"
  COMMAND = "command"
  SEARCH = "search"
  TUPLE = "tuple"
  URL = "url"
  VIEW_DEF = "viewDef"
  WORKSPACE = "workspace"


class View(Enum):
  CALENDAR = "calendar"
  LIST = "list"
  TABLE = "table"


class Props(BaseModel):
  created: int
  name: Optional[str]
  description: Optional[str]
  ownerId: Optional[str] = Field(alias='_ownerId')
  metaNodeId: Optional[str] = Field(alias='_metaNodeId')
  docType: Optional[PropType] = Field(alias='_docType')
  sourceId: Optional[str] = Field(alias='_sourceId')
  view: Optional[View]
  editMode: Optional[bool]
  done: Union[bool, int, None]


class Node(BaseModel):
  id: str
  props: Props
  touchCounts: Optional[List[int]]
  modifiedTs: Optional[List[int]]
  children: Optional[List[str]]
  associationMap: Optional[Dict[str, str]]
  underConstruction: Optional[bool]
  inbound_refs: List[str] = []
  outbound_refs: List[str] = []
  color: Optional[str] = None
  

class Visualizer(BaseModel):
  include_tag_nodes: bool = False
  include_inline_refs: bool = False
  include_inline_ref_nodes: bool = False
  
  # make this hashable
  class Config:
          frozen = True


class TanaDump(BaseModel):
  formatVersion: int
  docs: List[Node]
  editors: List[List[Union[int, str]]]
  workspaces: Dict[str, str]
  lastTxid: int
  lastFbKey: str
  optimisticTransIds: List[Any]
  currentWorkspaceId: str

  visualize: Optional[Visualizer] = None
