#-*- coding: utf-8 -*-
from openerp import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
    
#La forma más simple para agregar la lógica a un registro, es usar el decorador @api.one. 
#Aquí self representara un registro. 
#Si la acción es llamada para un conjunto de registros, la API gestionara esto lanzando el método para cada uno de los registros
#modifica el campo is_done, invirtiendo su valor. 
@api.one def do_toggle_done(self):
    self.is_done = not self.is_done		
    return True
	
@api.multi def do_clear_done(self):
    done_recs = self.search([('is_done', '=', True)])
    done_recs.write({'active': False})
    return True
