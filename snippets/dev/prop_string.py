# subtype (string) – Enumerator in ['FILE_PATH', 'DIR_PATH', 'FILE_NAME', 'BYTE_STRING', 'PASSWORD', 'NONE'].
# options (set) – Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
${1:bpy.types.Scene.}${2:String_variable_name} : ${3:bpy.props.}StringProperty(name="${4}", description="${5}", default="${6}", maxlen=0, options={'ANIMATABLE'}, subtype='NONE', update=None, get=None, set=None)${0}