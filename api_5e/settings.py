# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017

ITEM_METHODS = ['GET']
RESOURCE_METHODS = ['GET']

APPLICATION_ROOT = "/home/cslaf/5e-api-service"

MONGO_DBNAME = '5e-dnd'

choice_schema = {
    'type' : {
        'type' : 'string'
    },
    'choose' : {
        'type' : 'integer'
    },
    'from' : {
        'type' : 'list'
    },
}

simple_schema = {
     'name' : {
        'type' : 'string',
        'required' : True,
    },
    'desc' : {
        'type' : 'string',
    },
}

language_schema = {
    'name' : { 'type' : 'string', 'required' : True, },
    'type' : { 'type' : 'string' },
    'typical_speakers' : { 'type' : 'list'},
    'desc' : { 'type' : 'string' },
    'script' : { 'type' : 'string' },
}

monster_schema = {
    'name' : { 'type' : 'string'},
    'size' : { 'type' : 'string'},
    'type' : { 'type' : 'string'},
    'subtype' : { 'type' : 'string'},
    'alignment' : { 'type' : 'string'},
    'armor_class' : {'type': 'integer'},
    'hit_points' : {'type': 'integer'},
    'hit_dice' : { 'type' : 'string'},
    'speed' : { 'type' : 'string'},
    'reactions' : {'type' : 'list'},
    #I would like to make these a list of skills, but unsure if it's worth it
    'insight' : {'type': 'integer'},
    'persuasion' : {'type': 'integer'},
    'stealth' : { 'type' : 'integer'},
    'perception' : { 'type' : 'integer'},
    'arcana' : {'type' : 'integer' },
    'history' : {'type': 'integer'},
    'survival' : {'type': 'integer'},
    'deception' : {'type': 'integer'},
    'religion' : {'type': 'integer'},
    'intimidation' : {'type': 'integer'},
    'acrobatics' : {'type': 'integer'},
    'medicine' : {'type': 'integer'},
    'athletics' : {'type': 'integer'},
    'performance' : {'type': 'integer'},
    'nature' : {'type': 'integer'},
    'investigation' : {'type': 'integer'},
    #same with this and ability scores and saves
    'str' : {'type': 'integer'},
    'dex' : {'type': 'integer'},
    'con' : {'type': 'integer'},
    'int' : {'type': 'integer'},
    'wis' : {'type': 'integer'},
    'cha' : {'type': 'integer'},
    'str_save' : {'type': 'integer'},
    'dex_save' : {'type': 'integer'},
    'con_save' : {'type': 'integer'},
    'int_save' : {'type': 'integer'},
    'wis_save' : {'type': 'integer'},
    'cha_save' : {'type': 'integer'},
    'damage_vulnerabilities' : { 'type' : 'string'},
    'damage_resistances' : { 'type' : 'string'},
    'damage_immunities' : { 'type' : 'string'},
    'condition_immunities' : { 'type' : 'string'},
    'senses' : { 'type' : 'string'},
    'languages' : { 'type' : 'string'},
    'challenge_rating' : {'type': 'number'},
    'special_abilities' : {'type' : 'list'},
    'actions' : {'type': 'list'},
    'legendary_actions' : {'type': 'list'},
}

features_schema = {
    'name' : {
        'type' : 'string',
        'required' : True,
        'unique' : True,
    },
    'desc' : {
        'type' : 'string',
    },
    'level' : {
        'type' : 'integer',
    },
    'class' : {
        'type' : 'string',
    },
    'choice' : {
        'type' : 'dict',
        'schema' : choice_schema
    },
    'subclass' : {
        'type' : 'string',
        'nullable' : True,
    },
}

ability_score_schema = {
    'name' : {
        'type' : 'string',
        'required' : True,
        'unique' : True,
    },
    'full_name' : {
        'type' : 'string',
    },
    'desc' : {
        'type' : 'string'
    },
    'skills' : {
        'type' : 'list',
    }
}

subclass_schema = {
    'name' : { 'type' : 'string', 'required' : True, 'unique' : True },
    'class_name' : { 'type' : 'string', 'required' : True },
    'desc' : { 'type' : 'string' },
    'subclass_flavor' : { 'type' : 'string' },
    'features' : {
        'type' : 'list',
        'schema' : {
            'type' : 'dict',
            'schema' : features_schema
        },
    },
    'spells' : {
        'type' : 'list',
        'schema' : {
            'type' : 'dict',
            'schema' : { 'level_acquired' : { 'type' : 'integer'},
                        'spell' : { 'type' : 'string',
                                    'data_relation' : { 'resource' : 'spells', 'field' : 'name', 'embeddable' : True }
                                   },
                        'prereqs' : {'type' : 'list'}
                        }
        },
    },
}

class_level_schema = {
    'class_name' : {
        'type' : 'string',
        'required' : True,
    },
    'desc' : {
        'type' : 'string'
    },
    'level' : {
        'type' : 'integer',
        'required' : True,
    },
    'ability_score_bonuses' : {
        'type' : 'integer',
    },
    'prof_bonus' : {
        'type' : 'integer',
    },
    'feature_choices' : {
        'type' : 'list',
    },
    'spellcasting' : {
        'type' : 'dict',
    },
    'class_specific' : {
        'type' : 'dict',
    },
    'subclass_specific' : {
        'type' : 'dict',
    },
    'features' : {
        'type' : 'list',
        'schema' : {
            'type' : 'dict',
            'schema' : features_schema,
        },
    },
    'subclass' : {
        'type' : 'string',
    }
}

spellcasting_schema = {
    'class' : {
        'type' : 'string',
        'required' : True,
    },
    'level' : {
        'type' : 'integer',
    },
    'spellcasting_ability' : {
        'type' : 'string',
        'allowed' : ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'],
    },
    'info' : {
         'type' : 'list',
         'schema' : { 'type' : 'dict',
                    'schema' : simple_schema
                    },
    },
}

skill_schema = {
    'name' : {
        'type' : 'string',
        'required' : True,
        'unique' : True,
    },
    'desc' : {
        'type' : 'string',
    },
    'ability_score' : {
        'type' : 'string',
        'data_relation' : {
            'resource' : 'ability-scores',
            'field' : 'name',
            'embeddable' : True,
        },
    },
}

race_schema = {
    'name' : {'type' : 'string'},
    'alignment' : {'type' : 'string'},
    'age' : {'type' : 'string'},
    'size' : {'type' : 'string'},
    'size_desc' : {'type' : 'string'},
    'language_desc' : {'type' : 'string'},
    'speed' : {'type' : 'integer'},
    'ability_bonuses': { 'type' : 'list', 'schema' :
                        { 'type': 'dict',
                         'schema' : { 'name' : { 'type' : 'string', 'data_relation' : {'resource' : 'ability-scores', 'field' : 'name','embeddable' : True,}},
                                     'bonus' : { 'type' : 'integer'},
                                     }
                         }
                        },
    'ability_bonus_options' : {'schema' : choice_schema, },
    'starting_proficiencies' : { 'type' : 'list' },
    'languages' : { 'type' : 'list'},
    'language_options' : { 'schema' : choice_schema},
    'starting_proficiency_options' : { 'schema' : choice_schema },
    'traits' : { 'type' : 'list'},
    'trait_options' : {'schema' : choice_schema},
    'subraces' : { 'type' : 'list'},
}

equipment_schema = {
    'name' : {
        'type' : 'string',
        'required' : True,
        'unique' : True,
    },
    'desc' : {
        'type' : 'string',
    },
    'equipment_category' : {'type' : 'string' },
    'gear_category' : {'type' : 'string' },
    'weapon_category' : {'type' : 'string'},
    'weapon_range' : {'type' : 'string' },
    'category_range' : {'type' : 'string'},
    'armor_category' : {'type' : 'string'},
    'stealth_disadvantage' : {'type' : 'boolean'},
    'str_minimum' : {'type' : 'integer'},
    'cost' : {'type' : 'integer' },
    'weight' : {'type' : 'integer'},
    'armor_class' : {'type' : 'dict',
                    'schema':{
                            'base' : {'type' : 'integer'},
                            'dex_bonus' : {'type' : 'boolean'},
                            'max_bonus' : {'type' : 'integer'}
                            }
                     },
    'damage' : {'type' : 'dict',
                'schema':{
                            'dice_count' : {'type' : 'integer'},
                            'dice_value' : {'type' : 'integer'},
                            'damage_type' : {'type' : 'dict',
                                             'schema' : simple_schema },
                            },
                },
    '2h_damage' : {'type' : 'dict',
                'schema':{
                            'dice_count' : {'type' : 'integer'},
                            'dice_value' : {'type' : 'integer'},
                            'damage_type' : {'type' : 'dict',
                                             'schema' : simple_schema },
                            },
                },
    'properties' : {'type' : 'list',
                    'schema':{ 'type' : 'dict',
                               'schema' : simple_schema
                             },
                    },
    'range' : {'type' : 'dict',
                'schema':{ 'long' : {'type' : 'integer'},
                          'normal' : {'type' : 'integer'},
                          }
               },
    'throw_range' : {'type' : 'dict',
                'schema':{ 'long' : {'type' : 'integer'},
                          'normal' : {'type' : 'integer'},
                          }
               },
    'speed' : {'type' : 'dict'},
    'capacity' : {'type' : 'string'},
    'vehicle_category' : {'type' : 'string'},
    'tool_category' : {'type' : 'string'},
    'special' : {'type' : 'string'},
    'contents' : { 'type' : 'list',
                  'schema' : { 'type' : 'dict',
                               'schema' : {
                                   'name' : { 'type' : 'string'},
                                   'quantity': { 'type' : 'integer'},
                               },
                              },
                  },
}

class_schema = {
    'name' : {
        'type' : 'string',
        'required' : True,
        'unique' : True,
    },
    'description' : {
        'type' : 'string',
    },
    'hit_die' : {
        'type' : 'integer',
    },
    'proficiency_choices' : {
        'type' : 'dict',
        'schema' : choice_schema
    },
    'proficiencies' : {
        'type' : 'list',
    },
    'saving_throws' : {
        'type' : 'list',
    },
    'subclasses' : {
        'type' : 'list',
    },
    'spellcasting' : {
        'type' : 'dict',
        'schema' : spellcasting_schema,
    },
}

spell_schema = {
    'name' : {
        'type': 'string',
        'required' : True,
        'unique' : True,
    },
    'desc' : {
        'type' : 'string',
    },
    'higher_level' : {
        'type' : 'string',
    },
    'page' : {
        'type' : 'string',
    },
    'range' : {
        'type' : 'string',
    },
    'components' :{
        'type' : 'list',
        'allowed' : ["V", "S", "M"],
    },
    'material' : {
        'type' : 'string'
    },
    'ritual' : {
        'type': 'boolean',
    },
    'duration' : {
        'type' : 'string'
    },
    'concentration' : {
        'type' : 'boolean',
    },
    'casting_time' : {
        'type' : 'string',
    },
    'level' : {
        'type' : 'integer',
    },
    'school' : {
        'type' : 'string',
        'data_relation' : {
            'resource' : 'magic-schools',
            'field' : 'name',
            'embeddable' : True,
        },
    },
    'classes' : {
        'type' : 'list',
    },
    'subclasses' : {
        'type' : 'list',
    }
}

levels = {
    'additional_lookup' : {
       'url' :  'regex("[\w]+")',
        'field' : 'class_name'
    },
    'schema' : class_level_schema
}

classes = {
    'item_title' : "class",
    'additional_lookup' : {
        'url': 'regex("[\w]+")',
        'field' : 'name'
    },
    'schema' : class_schema
}

subclasses = {
    'item_title' : "subclass",
    'additional_lookup' : {
        'url': 'regex("[\w]+")',
        'field' : 'name'
    },
    'schema' : subclass_schema
}

ability_score = {
    'additional_lookup' : {
        'url': 'regex("[\w]+")',
        'field' : 'name'
    },
    'schema' : ability_score_schema
}

condition = {
    'additional_lookup' : {
        'url': 'regex("[\w]+")',
        'field' : 'name'
    },
    'schema' : simple_schema
}

magic_school = {
    'additional_lookup':{
        'url': 'regex("[\w]+")',
        'field': 'name'
    },
    'schema' : simple_schema
}
spell = {
    'additional_lookup':{
        'url': 'regex("[\w]+")',
        'field': 'name'
    },
    'schema' :spell_schema,
}

skill = {
    'additional_lookup':{
        'url': 'regex("[\w]+")',
        'field': 'name'
    },
    'schema' :skill_schema
}

proficiency = {
    'item_title' : "proficiency",
    'additional_lookup':{
        'url': 'regex("[\w]+")',
        'field': 'name'
    },
    'schema' :
    {
        'name' : { 'type' : 'string', 'required' : True },
        'type' : { 'type' : 'string'}
    },
}

equipment = {
    'item_title' : "equip",
    'additional_lookup':{
        'url': 'regex("[\w]+")',
        'field': 'name'
    },
    'schema' : equipment_schema
}

language = {
    'additional_lookup':{
        'url': 'regex("[\w]+")',
        'field': 'name'
    },
    'schema' : language_schema
}
race = {
    'additional_lookup':{
        'url': 'regex("[\w]+")',
        'field': 'name'
    },
    'schema' : race_schema
}

monster = {
    'additional_lookup':{
        'url': 'regex("[\w]+")',
        'field': 'name'
    },
    'schema' : monster_schema
}

DOMAIN = {
    'spells': spell,
    'magic-schools' : magic_school,
    'ability-scores' : ability_score,
    'skills' : skill,
    'classes' : classes,
    'subclasses' : subclasses,
    'races' : race,
    'monsters' : monster,
    'languages' : language,
    'equipment' : equipment,
    'proficiencies' : proficiency,
    'conditions' : condition,
    'levels' : levels,
}
