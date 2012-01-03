//
//  Section.h
//  Qcumber
//
//  Created by Chris Cooper on 11-12-31.
//  Copyright (c) 2011 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>

#import "Term.h"
#import "SectionType.h"

@interface Section : NSObject

@property (assign) int index;
@property (assign) int id;

@property (weak) Term *term;
@property (weak) SectionType *type;
@property (strong) NSArray *components;

@end
