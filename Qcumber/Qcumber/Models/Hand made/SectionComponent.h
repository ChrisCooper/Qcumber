//
//  SectionComponent.h
//  Qcumber
//
//  Created by Chris Cooper on 11-12-31.
//  Copyright (c) 2011 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>
#include "Timeslot.h"

@interface SectionComponent : NSObject

@property (strong) NSString *room;
@property (strong) NSString *instructor;
@property (strong) NSString *startDate;
@property (strong) NSString *endDate;
@property (weak) Timeslot *timeslot;

@end
